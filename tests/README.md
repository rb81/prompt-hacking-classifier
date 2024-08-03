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

## Conducting Your Own Tests

To conduct your own tests, you can use the test cases files as demonstrated in the [`ollama_tests.ipynb`](/tests/ollama_tests.ipynb) and  [`openai_tests.ipynb`](/tests/openai_tests.ipynb) notebooks.