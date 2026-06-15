#!/usr/bin/env python3
"""
Quick script to regenerate test_results.md from cached data
"""

import json
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
ROOT_DIR = SCRIPTS_DIR.parent
CACHE_DIR = ROOT_DIR / ".cache" / "test"
RESULTS_DIR = ROOT_DIR / "results"
RESULTS_FILE = RESULTS_DIR / "test_results.md"

def calculate_metrics(results):
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
    
    tp = sum(1 for r in valid_results if r["expected"] == "true" and r["predicted"] == "true")
    tn = sum(1 for r in valid_results if r["expected"] == "false" and r["predicted"] == "false")
    fp = sum(1 for r in valid_results if r["expected"] == "false" and r["predicted"] == "true")
    fn = sum(1 for r in valid_results if r["expected"] == "true" and r["predicted"] == "false")
    
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


def generate_results_report(all_results):
    """Generate results report from cached data"""
    print(f"\nGenerating Results Report from {len(all_results)} cached model(s)...")
    
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    model_metrics = []
    for model, data in all_results:
        metrics = calculate_metrics(data["results"])
        model_metrics.append({
            "model": model,
            **metrics
        })
    
    model_metrics.sort(key=lambda x: (-x["f1"], -x["accuracy"], x["avg_time"]))
    
    report = ["# Prompt Hacking Classifier - Test Results\n"]
    report.append(f"**Total Models Tested:** {len(model_metrics)}\n")
    report.append(f"**Test Cases:** {model_metrics[0]['total'] if model_metrics else 0}\n")
    report.append("")
    
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
    
    report.append("## Summary\n")
    
    if model_metrics:
        best = model_metrics[0]
        report.append(f"**Best Overall Model:** {best['model']}")
        report.append(f"- F1 Score: {best['f1']:.4f}")
        report.append(f"- Accuracy: {best['accuracy']:.4f}")
        report.append(f"- Precision: {best['precision']:.4f}")
        report.append(f"- Recall: {best['recall']:.4f}")
        report.append(f"- Avg Inference Time: {best['avg_time']:.2f}s\n")
        
        fast_accurate = [m for m in model_metrics if m["f1"] >= 0.90]
        if fast_accurate:
            fastest = min(fast_accurate, key=lambda x: x["avg_time"])
            report.append(f"**Fastest Accurate Model** (F1 ≥ 0.90): {fastest['model']}")
            report.append(f"- Avg Inference Time: {fastest['avg_time']:.2f}s")
            report.append(f"- F1 Score: {fastest['f1']:.4f}\n")
    
    with open(RESULTS_FILE, "w") as f:
        f.write("\n".join(report))
    
    print(f"✓ Results saved to {RESULTS_FILE}")


def main():
    """Load all cache files and regenerate report"""
    if not CACHE_DIR.exists():
        print(f"❌ Error: No cache directory found ({CACHE_DIR}/)")
        return
    
    cache_files = list(CACHE_DIR.glob("*.json"))
    if not cache_files:
        print(f"❌ Error: No cache files found in {CACHE_DIR}/")
        return
    
    print(f"Found {len(cache_files)} cached model(s)")
    
    all_results = []
    for cache_file in cache_files:
        with open(cache_file, "r") as f:
            data = json.load(f)
            if data.get("completed", False):
                all_results.append((data["model"], data))
                print(f"  ✓ {data['model']}: {len(data['results'])} test cases")
            else:
                print(f"  ⚠ {data['model']}: incomplete (skipping)")
    
    if not all_results:
        print("\n❌ Error: No completed models found in cache")
        return
    
    generate_results_report(all_results)
    print(f"\n✅ Done! Check {RESULTS_FILE}")


if __name__ == "__main__":
    main()
