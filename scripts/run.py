#!/usr/bin/env python3
"""
Prompt Hacking Classifier - Test Runner
Evaluates Ollama models on their ability to detect prompt injection attacks.
"""

import argparse
import json
import os
import re
import shutil
import signal
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: 'python-dotenv' package not found. Install it with: pip install python-dotenv")
    exit(1)

try:
    from ollama import Client
except ImportError:
    print("Error: 'ollama' package not found. Install it with: pip install ollama")
    exit(1)

# Load environment variables from .env file
load_dotenv()


# Global flag for graceful shutdown
INTERRUPTED = False


def signal_handler(sig, frame):
    """Handle interrupt signals gracefully"""
    global INTERRUPTED
    INTERRUPTED = True
    print("\n\n⚠️  Interrupt received. Finishing current test and saving progress...")
    print("   Press Ctrl+C again to force quit (progress will be saved)")


# Configuration
SCRIPTS_DIR = Path(__file__).parent
ROOT_DIR = SCRIPTS_DIR.parent
CACHE_DIR = ROOT_DIR / ".cache" / "test"
RESULTS_DIR = ROOT_DIR / "results"
MODELS_FILE = SCRIPTS_DIR / "models.txt"
TEST_CASES_FILE = SCRIPTS_DIR / "test-cases.json"
CLASSIFIER_PROMPT_FILE = ROOT_DIR / "classifier.prompt"
RESULTS_FILE = RESULTS_DIR / "test_results.md"
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "localhost:11434")
OLLAMA_TIMEOUT = int(os.environ.get("OLLAMA_TIMEOUT", "120"))

# Hyperparameters for classification
GENERATION_OPTIONS = {
    "num_predict": 512,
    "temperature": 0.0,
    "top_k": 2,
    "top_p": 0.8
}


def load_models() -> List[str]:
    """Load model list from models.txt"""
    if not MODELS_FILE.exists():
        print(f"Error: {MODELS_FILE} not found")
        exit(1)
    
    with open(MODELS_FILE, "r") as f:
        models = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    
    print(f"✓ Loaded {len(models)} models from {MODELS_FILE}")
    return models


def load_test_cases() -> List[Dict]:
    """Load test cases from test-cases.json"""
    if not TEST_CASES_FILE.exists():
        print(f"Error: {TEST_CASES_FILE} not found")
        exit(1)
    
    with open(TEST_CASES_FILE, "r") as f:
        test_cases = json.load(f)
    
    malicious_count = sum(1 for tc in test_cases if tc["expected_classification"] == "true")
    benign_count = len(test_cases) - malicious_count
    
    print(f"✓ Loaded {len(test_cases)} test cases ({malicious_count} malicious, {benign_count} benign)")
    return test_cases


def load_classifier_prompt() -> str:
    """Load classifier prompt template"""
    if not CLASSIFIER_PROMPT_FILE.exists():
        print(f"Error: {CLASSIFIER_PROMPT_FILE} not found")
        exit(1)
    
    with open(CLASSIFIER_PROMPT_FILE, "r") as f:
        prompt = f.read()
    
    print(f"✓ Loaded classifier prompt from {CLASSIFIER_PROMPT_FILE}")
    return prompt


def test_ollama_connection(host: str, timeout: int = 5) -> bool:
    """Test if Ollama server is reachable"""
    try:
        client = Client(host=host, timeout=timeout)
        # Try to list models to verify connection
        client.list()
        return True
    except Exception as e:
        return False


def safe_model_name(model: str) -> str:
    """Convert model name to safe filename"""
    return re.sub(r'[^a-zA-Z0-9_-]', '_', model)


def load_cached_results(model: str) -> Dict:
    """Load cached results for a model if they exist"""
    cache_file = CACHE_DIR / f"{safe_model_name(model)}.json"
    
    if cache_file.exists():
        with open(cache_file, "r") as f:
            return json.load(f)
    
    return {"model": model, "results": [], "completed": False}


def save_cached_results(model: str, data: Dict):
    """Save results to cache"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"{safe_model_name(model)}.json"
    
    with open(cache_file, "w") as f:
        json.dump(data, f, indent=2)


def parse_model_response(raw_response: str) -> str:
    """
    Parse model response to extract 'true' or 'false', handling:
    - <think>...</think> blocks (thinking models like deepseek-r1, qwen3)
    - Reasoning prefixes before the actual answer
    - Markdown formatting, quotes, punctuation
    - Verbose responses like "The answer is true"
    """
    text = raw_response.strip()
    
    # Remove <think>...</think> blocks (thinking models)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()
    
    # Remove any remaining XML-like tags
    text = re.sub(r'<[^>]+>', '', text).strip()
    
    # Remove markdown formatting (bold, code blocks, etc.)
    text = re.sub(r'[`*_]', '', text).strip()
    
    # Remove common prefixes like "Answer:", "Classification:", "Result:"
    text = re.sub(r'^(answer|classification|result|response|output)\s*[:=]\s*', '', text, flags=re.IGNORECASE).strip()
    
    # Remove quotation marks
    text = text.strip('"\'')
    
    # Convert to lowercase for matching
    text_lower = text.lower()
    
    # Direct match (most common case for well-behaved models)
    if text_lower in ('true', 'false'):
        return text_lower
    
    # Check if the response starts with true/false (e.g., "true." or "true\n\nExplanation...")
    if text_lower.startswith('true'):
        return 'true'
    if text_lower.startswith('false'):
        return 'false'
    
    # Check if response ends with true/false (e.g., "Based on analysis: true")
    if text_lower.endswith('true'):
        return 'true'
    if text_lower.endswith('false'):
        return 'false'
    
    # Search for the words in the response (last resort)
    # Prefer the last occurrence as it's likely the final answer
    true_pos = text_lower.rfind('true')
    false_pos = text_lower.rfind('false')
    
    if true_pos >= 0 and false_pos >= 0:
        # Both found - take the one that appears last (likely the conclusion)
        return 'true' if true_pos > false_pos else 'false'
    elif true_pos >= 0:
        return 'true'
    elif false_pos >= 0:
        return 'false'
    
    return 'unknown'


def classify_statement(client: Client, model: str, prompt_template: str, statement: str) -> Tuple[str, float]:
    """
    Classify a single statement using the model.
    Returns (prediction, inference_time)
    """
    final_prompt = prompt_template.replace("{{USER_MESSAGE}}", statement)
    
    start_time = time.time()
    try:
        response = client.chat(
            model=model,
            messages=[{"role": "user", "content": final_prompt}],
            options=GENERATION_OPTIONS
        )
        inference_time = time.time() - start_time
        
        # Extract and parse prediction from content field
        raw_response = response["message"]["content"]
        prediction = parse_model_response(raw_response)
        
        # If content was empty/unknown, try the thinking field as fallback
        if prediction == "unknown" and "thinking" in response.get("message", {}):
            thinking_content = response["message"]["thinking"]
            if thinking_content:
                prediction = parse_model_response(thinking_content)
        
        return prediction, inference_time
    
    except Exception as e:
        inference_time = time.time() - start_time
        print(f"\n  ⚠ Error: {str(e)}")
        return "error", inference_time


def warmup_model(client: Client, model: str, prompt_template: str):
    """Send a warmup request using the actual prompt template to cache the prefix"""
    print(f"🔥 Warming up {model}...", end="", flush=True)
    try:
        warmup_prompt = prompt_template.replace("{{USER_MESSAGE}}", "Hello")
        client.chat(
            model=model,
            messages=[{"role": "user", "content": warmup_prompt}],
            options=GENERATION_OPTIONS
        )
        print(" ✓ Model loaded")
    except Exception as e:
        print(f" ⚠ Warmup failed: {str(e)}")


def test_model(client: Client, model: str, prompt_template: str, test_cases: List[Dict]) -> Dict:
    """Test a single model on all test cases"""
    global INTERRUPTED
    
    print(f"\n{'='*70}")
    print(f"Testing: {model}")
    print(f"{'='*70}")
    
    # Load or initialize cache
    cached_data = load_cached_results(model)
    
    if cached_data["completed"]:
        print(f"✓ Model already completed (using cached results)")
        return cached_data
    
    # Warm up the model (load into memory and cache prompt prefix)
    warmup_model(client, model, prompt_template)
    
    # Resume from where we left off
    start_index = len(cached_data["results"])
    if start_index > 0:
        print(f"↻ Resuming from test case {start_index + 1}/{len(test_cases)}")
    
    results = cached_data["results"]
    
    for idx in range(start_index, len(test_cases)):
        # Check if interrupted
        if INTERRUPTED:
            print(f"\n\n⏸️  Paused at test case {idx + 1}/{len(test_cases)}")
            print(f"   Progress saved. Run again to resume from this point.")
            return cached_data
        
        test_case = test_cases[idx]
        statement = test_case["statement"]
        expected = test_case["expected_classification"]
        
        # Progress indicator
        progress = f"[{idx + 1}/{len(test_cases)}]"
        statement_preview = statement[:50] + "..." if len(statement) > 50 else statement
        print(f"{progress} Testing: {statement_preview}", end="", flush=True)
        
        prediction, inference_time = classify_statement(client, model, prompt_template, statement)
        
        result = {
            "statement": statement,
            "expected": expected,
            "predicted": prediction,
            "correct": prediction == expected,
            "inference_time": inference_time
        }
        
        results.append(result)
        
        # Show result
        status = "✓" if result["correct"] else "✗"
        print(f" → {status} ({inference_time:.2f}s)")
        
        # Save progress after each test
        cached_data["results"] = results
        save_cached_results(model, cached_data)
    
    # Mark as completed
    cached_data["completed"] = True
    save_cached_results(model, cached_data)
    
    print(f"\n✓ Completed testing {model}")
    return cached_data


def calculate_metrics(results: List[Dict]) -> Dict:
    """Calculate accuracy, precision, recall, F1, and average inference time"""
    if not results:
        return {
            "total": 0,
            "correct": 0,
            "accuracy": 0.0,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "avg_time": 0.0,
            "errors": 0
        }
    
    # Filter out errors
    valid_results = [r for r in results if r["predicted"] != "error"]
    error_count = len(results) - len(valid_results)
    
    if not valid_results:
        return {
            "total": len(results),
            "correct": 0,
            "accuracy": 0.0,
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
            "avg_time": sum(r["inference_time"] for r in results) / len(results),
            "errors": error_count
        }
    
    # Calculate confusion matrix
    tp = sum(1 for r in valid_results if r["expected"] == "true" and r["predicted"] == "true")
    tn = sum(1 for r in valid_results if r["expected"] == "false" and r["predicted"] == "false")
    fp = sum(1 for r in valid_results if r["expected"] == "false" and r["predicted"] == "true")
    fn = sum(1 for r in valid_results if r["expected"] == "true" and r["predicted"] == "false")
    
    # Metrics
    accuracy = (tp + tn) / len(valid_results) if valid_results else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    avg_time = sum(r["inference_time"] for r in valid_results) / len(valid_results)
    
    return {
        "total": len(results),
        "correct": tp + tn,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "avg_time": avg_time,
        "errors": error_count
    }


def parse_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Prompt Hacking Classifier - Test Runner for Ollama models",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                           # Normal run (uses cache)
  python run.py --clear-cache             # Clear all cache and rerun everything
  python run.py --clear-model "gemma3:4b" # Clear cache for specific model only
        """
    )
    
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear all cached results before running (forces complete rerun)"
    )
    
    parser.add_argument(
        "--clear-model",
        type=str,
        metavar="MODEL",
        help="Clear cached results for a specific model only"
    )
    
    return parser.parse_args()


def clear_cache(model: str = None):
    """Clear cached results"""
    if model:
        # Clear specific model cache
        cache_file = CACHE_DIR / f"{safe_model_name(model)}.json"
        if cache_file.exists():
            cache_file.unlink()
            print(f"✓ Cleared cache for model: {model}")
        else:
            print(f"⚠ No cache found for model: {model}")
    else:
        # Clear entire cache directory
        if CACHE_DIR.exists():
            shutil.rmtree(CACHE_DIR)
            print(f"✓ Cleared all cached results from {CACHE_DIR}/")
        else:
            print(f"⚠ No cache directory found ({CACHE_DIR}/ does not exist)")


def generate_results_report(all_results: List[Tuple[str, Dict]]):
    """Generate results report"""
    print(f"\n{'='*70}")
    print("Generating Results Report")
    print(f"{'='*70}")
    
    # Ensure results directory exists
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Calculate metrics for each model
    model_metrics = []
    for model, data in all_results:
        metrics = calculate_metrics(data["results"])
        model_metrics.append({
            "model": model,
            **metrics
        })
    
    # Sort by F1 (desc), then Accuracy (desc), then Avg Time (asc)
    model_metrics.sort(key=lambda x: (-x["f1"], -x["accuracy"], x["avg_time"]))
    
    # Generate markdown
    report = ["# Prompt Hacking Classifier - Test Results\n"]
    report.append(f"**Total Models Tested:** {len(model_metrics)}\n")
    report.append(f"**Test Cases:** {model_metrics[0]['total'] if model_metrics else 0}\n")
    report.append("")
    
    # Leaderboard
    report.append("## Leaderboard\n")
    report.append("| Rank | Model | Accuracy | Precision | Recall | F1 Score | Avg Time (s) | Errors |")
    report.append("|:----:|:------|:--------:|:---------:|:------:|:--------:|:------------:|:------:|")
    
    for rank, m in enumerate(model_metrics, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else f"{rank}"
        report.append(
            f"| {medal} | {m['model']} | {m['accuracy']:.4f} | {m['precision']:.4f} | "
            f"{m['recall']:.4f} | {m['f1']:.4f} | {m['avg_time']:.2f} | {m['errors']} |"
        )
    
    report.append("")
    
    # Tier categorization
    report.append("## Performance Tiers\n")
    
    excellent = [m for m in model_metrics if m["f1"] >= 0.95]
    good = [m for m in model_metrics if 0.85 <= m["f1"] < 0.95]
    fair = [m for m in model_metrics if 0.70 <= m["f1"] < 0.85]
    poor = [m for m in model_metrics if m["f1"] < 0.70]
    
    if excellent:
        report.append("### Excellent (F1 ≥ 0.95)\n")
        for m in excellent:
            report.append(f"- **{m['model']}**: F1={m['f1']:.4f}, Accuracy={m['accuracy']:.4f}")
        report.append("")
    
    if good:
        report.append("### Good (0.85 ≤ F1 < 0.95)\n")
        for m in good:
            report.append(f"- **{m['model']}**: F1={m['f1']:.4f}, Accuracy={m['accuracy']:.4f}")
        report.append("")
    
    if fair:
        report.append("### Fair (0.70 ≤ F1 < 0.85)\n")
        for m in fair:
            report.append(f"- **{m['model']}**: F1={m['f1']:.4f}, Accuracy={m['accuracy']:.4f}")
        report.append("")
    
    if poor:
        report.append("### Poor (F1 < 0.70)\n")
        for m in poor:
            report.append(f"- **{m['model']}**: F1={m['f1']:.4f}, Accuracy={m['accuracy']:.4f}")
        report.append("")
    
    # Summary
    report.append("## Summary\n")
    
    if model_metrics:
        best = model_metrics[0]
        report.append(f"**Best Overall Model:** {best['model']}")
        report.append(f"- F1 Score: {best['f1']:.4f}")
        report.append(f"- Accuracy: {best['accuracy']:.4f}")
        report.append(f"- Precision: {best['precision']:.4f}")
        report.append(f"- Recall: {best['recall']:.4f}")
        report.append(f"- Avg Inference Time: {best['avg_time']:.2f}s\n")
        
        # Fastest accurate model (F1 > 0.90)
        fast_accurate = [m for m in model_metrics if m["f1"] >= 0.90]
        if fast_accurate:
            fastest = min(fast_accurate, key=lambda x: x["avg_time"])
            report.append(f"**Fastest Accurate Model** (F1 ≥ 0.90): {fastest['model']}")
            report.append(f"- Avg Inference Time: {fastest['avg_time']:.2f}s")
            report.append(f"- F1 Score: {fastest['f1']:.4f}\n")
    
    report.append("## Key Metrics Explained\n")
    report.append("- **Accuracy**: Proportion of correct predictions (both true and false)")
    report.append("- **Precision**: Of all predicted attacks, how many were actual attacks")
    report.append("- **Recall**: Of all actual attacks, how many were detected")
    report.append("- **F1 Score**: Harmonic mean of precision and recall (balanced metric)")
    report.append("- **Avg Time**: Average inference time per test case in seconds")
    
    # Write report
    with open(RESULTS_FILE, "w") as f:
        f.write("\n".join(report))
    
    print(f"✓ Results saved to {RESULTS_FILE}")


def main():
    """Main execution"""
    global INTERRUPTED
    
    # Parse command-line arguments
    args = parse_args()
    
    # Setup signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        print("\n" + "="*70)
        print("PROMPT HACKING CLASSIFIER - TEST RUNNER")
        print("="*70 + "\n")
        
        # Handle cache clearing if requested
        if args.clear_cache:
            clear_cache()
            print()
        elif args.clear_model:
            clear_cache(model=args.clear_model)
            print()
        
        # Load configuration
        models = load_models()
        test_cases = load_test_cases()
        prompt_template = load_classifier_prompt()
        
        # Test Ollama connection
        print(f"\n🔌 Testing connection to Ollama at {OLLAMA_HOST}...", end="", flush=True)
        if not test_ollama_connection(OLLAMA_HOST):
            print(" ✗ FAILED\n")
            print("❌ Error: Could not connect to Ollama server.")
            print(f"   Make sure Ollama is running at {OLLAMA_HOST}")
            print("\n   To start Ollama:")
            print("   1. Run: ollama serve")
            print("   2. Or check if Ollama is running: ps aux | grep ollama")
            print(f"   3. Verify the host address (currently: {OLLAMA_HOST})")
            sys.exit(1)
        print(" ✓ Connected")
        
        # Initialize Ollama client
        client = Client(host=OLLAMA_HOST, timeout=OLLAMA_TIMEOUT)
        
        # Test each model
        all_results = []
        
        for model in models:
            if INTERRUPTED:
                print("\n\n⏸️  Test run interrupted by user.")
                break
            
            try:
                result = test_model(client, model, prompt_template, test_cases)
                all_results.append((model, result))
            except KeyboardInterrupt:
                # Second Ctrl+C for force quit
                print("\n\n❌ Force quit requested. Progress has been saved.")
                break
            except Exception as e:
                print(f"\n✗ Failed to test {model}: {str(e)}")
                print("  Continuing with next model...")
                continue
        
        # Generate report if we have results
        if all_results and not INTERRUPTED:
            generate_results_report(all_results)
            
            print("\n" + "="*70)
            print("✓ ALL TESTS COMPLETED")
            print("="*70)
            print(f"\nResults saved to: {RESULTS_FILE}")
            print(f"Cached data stored in: {CACHE_DIR}/")
        elif all_results:
            # Partial results
            generate_results_report(all_results)
            print("\n" + "="*70)
            print("⏸️  TESTS INTERRUPTED (Partial Results Saved)")
            print("="*70)
            print(f"\nPartial results saved to: {RESULTS_FILE}")
            print(f"Cached data stored in: {CACHE_DIR}/")
            print(f"\n💡 Run again to continue from where you left off.")
        else:
            print("\n✗ No results to report")
    
    except KeyboardInterrupt:
        print("\n\n❌ Interrupted. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
