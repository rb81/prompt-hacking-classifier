# Test Results

## Test Parameters

**Accuracy:**

- Proportion of correct predictions (both true positives and true negatives) to the total number of predictions.
- **Formula:** (True Positives + True Negatives) / (Total Predictions)
- **Meaning:** It measures how often the model is correct overall. Higher accuracy means the model is more reliable in general.

**Precision:**

- Proportion of true positive predictions to the total number of positive predictions.
- **Formula:** True Positives / (True Positives + False Positives)
- **Meaning:** Precision indicates how many of the predicted positive instances were actually true positives. Higher precision means fewer false positives.

**Recall (Sensitivity or True Positive Rate):**

- Proportion of true positive predictions to the total actual positive instances.
- **Formula:** True Positives / (True Positives + False Negatives)
- **Meaning:** Recall measures the model’s ability to identify all actual positive instances. Higher recall means fewer false negatives.

**F1 Score:**

- Harmonic mean of precision and recall.
- **Formula:** 2 * (Precision * Recall) / (Precision + Recall)
- **Meaning:** The F1 Score provides a single metric that balances both precision and recall. It is particularly useful when you need to balance both false positives and false negatives.

**Time (s) - Average Inference Time:**

- The average processing time (in seconds) per query for the model.
- **Meaning:** Reflects the computational efficiency and responsiveness of the model. Lower times are generally better if real-time performance is crucial.

**Fails - Failure Rate (Open Models):**

- Number of tests where the model took more than 60 seconds to respond. (Does not apply to OpenAI models.)
- **Meaning:** Indicates the reliability of the model. More failed tests usually signal decreased reliability.

## Results

### OpenAI Models

| Model Name                 | Accuracy | Precision | Recall   | F1 Score | Time (s) |
|:---------------------------|:---------|:----------|:---------|:---------|---------:|
| gpt-3.5-turbo (Fine-Tuned) | 0.992647 | 0.986301  | 1        | 0.993103 | 0.527184 |
| gpt-3.5-turbo              | 0.992647 | 0.986301  | 1        | 0.993103 | 0.554754 |
| gpt-4                      | 0.977941 | 0.985915  | 0.972222 | 0.979021 | 0.713412 |
| gpt-4-turbo                | 0.948529 | 1         | 0.902778 | 0.948905 | 0.710608 |
| gpt-4o                     | 0.977941 | 1         | 0.958333 | 0.978723 | 0.552098 |

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

## Conducting Your Own Tests

To conduct your own tests, you can use the [`test_cases.json`](/tests/test_cases.json) file as demonstrated in the [`openmodel_tests.ipynb`](/tests/openmodel_tests.ipynb) and  [`openai_tests.ipynb`](/tests/openai_tests.ipynb) notebooks.