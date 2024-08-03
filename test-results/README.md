# Summaries of Test Results

## v1

### OpenAI Models

| Model Name                 | Accuracy | Precision | Recall   | F1 Score | Time (s) |
|:---------------------------|:---------|:----------|:---------|:---------|---------:|
| gpt-3.5-turbo (Fine-Tuned) | 0.992647 | 0.986301  | 1        | 0.993103 | 0.527184 |
| gpt-3.5-turbo              | 0.992647 | 0.986301  | 1        | 0.993103 | 0.554754 |
| gpt-4                      | 0.977941 | 0.985915  | 0.972222 | 0.979021 | 0.713412 |
| gpt-4-turbo                | 0.948529 | 1         | 0.902778 | 0.948905 | 0.710608 |
| gpt-4o                     | 0.977941 | 1         | 0.958333 | 0.978723 | 0.552098 |

For detailed reports, please see [/test-results/ollama_results/v1/](/test-results/ollama_results/v1/).

### Open Models (Ollama)

| Model             | Params (B) | Accuracy | Precision | Recall   | F1 Score | Time (s) | Fails |
|:------------------|:-----------|:---------|:----------|:---------|:---------|:---------|:------|
| phi3              | 3.8        | 0.977778 | 0.96      | 1        | 0.979592 | 5.28389  |     1 |
| qwen2             | 7          | 0.977778 | 1         | 0.958333 | 0.978723 | 6.40025  |     1 |
| qwen2             | 1.5        | 0.963235 | 0.946667  | 0.986111 | 0.965986 | 1.48894  |     0 |
| openchat          | 7          | 0.948529 | 1         | 0.902778 | 0.948905 | 8.063    |     0 |
| mistral           | 7          | 0.867647 | 0.965517  | 0.777778 | 0.861538 | 7.90731  |     0 |
| aya               | 8          | 0.772059 | 1         | 0.569444 | 0.725664 | 10.0726  |     0 |
| qwen2             | 0.5        | 0.529412 | 0.529412  | 1        | 0.692308 | 0.624812 |     0 |
| llama2            | 7          | 0.522388 | 0.522388  | 1        | 0.686275 | 7.86038  |     2 |
| llama3            | 8          | 0.713235 | 1         | 0.458333 | 0.628571 | 7.10806  |     0 |
| llava             | 7          | 0.676471 | 0.9375    | 0.416667 | 0.576923 | 7.89053  |     0 |
| wizardlm2         | 7          | 0.643939 | 1         | 0.318841 | 0.483516 | 8.42673  |     4 |
| gemma             | 2          | 0.455882 | 0.480769  | 0.347222 | 0.403226 | 2.11025  |     0 |
| orca-mini         | 7          | 0.21374  | 0.307692  | 0.411765 | 0.352201 | 9.75878  |     5 |
| orca-mini         | 3          | 0.0588235| 0.111111  | 0.111111 | 0.111111 | 3.83224  |     0 |
| llama3-gradient   | 8          | 0.477941 | 1         | 0.0138889| 0.027397 | 7.08649  |     0 |
| llama3-chatqa     | 8          | 0.474074 | 0         | 0        | 0        | 12.5904  |     1 |
| zephyr            | 7          | 0.11194  | 0         | 0        | 0        | 12.5892  |     2 |
| gemma             | 7          | 0.00735294| 0        | 0        | 0        | 7.85601  |     0 |
| tinydolphin       | 1.1        | 0        | 0         | 0        | 0        | 1.47554  |     0 |
| tinyllama         | 1.1        | 0        | 0         | 0        | 0        | 1.47945  |     2 |
| stablelm2         | 1.6        | 0        | 0         | 0        | 0        | 3.26776  |     0 |
| phi               | 2.7        | 0        | 0         | 0        | 0        | 3.60273  |     2 |
| falcon            | 7          | 0        | 0         | 0        | 0        | 7.20842  |     0 |
| orca2             | 7          | 0        | 0         | 0        | 0        | 8.16587  |     2 |
| samantha-mistral  | 7          | 0        | 0         | 0        | 0        | 8.46869  |     2 |
| nous-hermes       | 7          | 0        | 0         | 0        | 0        | 13.8335  |     1 |

**Ordering Logic:** Results were ordered first by `F1 Score`, then `Accuracy Rate`, then `Average Inference Time`, and finally `Fail Rate`.

For detailed reports, please see [/test-results/openai_results/v1/](/test-results/openai_results/v1/).

## v2

Coming soon.

## Hardware & Software

Open models were tested on a relatively simple, cost-effective machine with the following specifications, running Ubuntu Server and Ollama:

| Specification  | Details                             |
|:---------------|:------------------------------------|
| Computer Model | Dell Vostro 3910                    |
| Processor      | 12th Gen Intel(R) Core(TM) i7-12700 |
| RAM            | 64GB                                |
| GPU            | None                                |

**Note:** The hardware listed above costs approximately $600. With better hardware the solution can be expected to perform much better.

## Interpreting Results

To interpret varying scores effectively:

1. **Accuracy Variability:** A lower accuracy score vs higher accuracy in might indicate overfitting or an inability to generalize.
2. **False Positives and Negatives:** Pay close attention to precision and recall scores. High precision with low recall suggests the model misses many true positives, whereas high recall with low precision could indicate a significant number of false positives.
3. **Prior Validation:** Conduct validations in controlled environments and consider real-world inputs that might not have been covered in initial testing before deploying in sensitive or critical systems.

## Limitations

While the initial tests provided valuable insights, there are a number of limitations to consider:

- Tests were conducted using 100 test cases, and did not include emojis, ASCII art, or more sophisticated attack methods.
- The hardware used to test the open models negatively impacted inference times substantially.
- Larger open models that would likely deliver much better results were excluded due to hardware limitations