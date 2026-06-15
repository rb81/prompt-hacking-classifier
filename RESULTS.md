# Prompt Effectiveness Experiment - Comprehensive Report

**Models Tested:** 35

**Conditions:** Full Prompt vs Lite Prompt vs No Prompt (Raw)


## 🎯 Executive Summary

- **Full Prompt wins:** 7 models
- **Lite Prompt wins:** 26 models
- **Ties:** 2 models

**Average Prompt Value:** 0.5847 (F1 gain over no-prompt)

## 📊 Model-by-Model Comparison

| Model | Full F1 | Lite F1 | No-Prompt Resist% | Prompt Value | Winner |
|:------|:-------:|:-------:|:----------------:|:------------:|:------:|
| gpt-oss:20b | 0.9714 | 0.9635 | 0.0% | +0.9714 | Full |
| gemma3n:e4b | 0.9403 | 0.9559 | 0.0% | +0.9403 | Lite |
| gemma4:e4b | 0.9028 | 0.9784 | 0.0% | +0.9028 | Lite |
| ministral-3:8b | 0.8906 | 0.9252 | 0.0% | +0.8906 | Lite |
| gemma3:4b | 0.8732 | 0.9079 | 0.0% | +0.8732 | Lite |
| qwen3:8b | 0.8640 | 0.9160 | 0.0% | +0.8640 | Lite |
| granite4.1:8b | 0.8099 | 0.9565 | 0.0% | +0.8099 | Lite |
| deepseek-r1:8b | 0.7931 | 0.9323 | 0.0% | +0.7931 | Lite |
| lfm2.5:8b | 0.6379 | 0.7368 | 0.0% | +0.6379 | Lite |
| mistral:7b | 0.6286 | 0.8571 | 0.0% | +0.6286 | Lite |
| smallthinker:3b | 0.6226 | 0.5918 | 0.0% | +0.6226 | Full |
| cogito:8b | 0.6154 | 0.9007 | 0.0% | +0.6154 | Lite |
| gemma3:270m | 0.6121 | 0.6244 | 0.0% | +0.6121 | Lite |
| smollm2:135m | 0.6118 | 0.5683 | 0.0% | +0.6118 | Full |
| smollm2:1.7b | 0.6061 | 0.5517 | 0.0% | +0.6061 | Full |
| llama3.2:1b | 0.5939 | 0.0000 | 0.0% | +0.5939 | Full |
| qwen3.5:9b | 0.5440 | 0.8872 | 0.0% | +0.5440 | Lite |
| phi4:14b | 0.4565 | 0.9635 | 0.0% | +0.4565 | Lite |
| deepseek-r1:1.5b | 0.4118 | 0.3932 | 0.0% | +0.4118 | Full |
| granite4.1:3b | 0.3678 | 0.8264 | 0.0% | +0.3678 | Lite |
| qwen3.5:0.8b | 0.1690 | 0.1429 | 0.0% | +0.1690 | Full |
| granite4:350m | 0.0548 | 0.6121 | 0.0% | +0.0548 | Lite |
| hermes3:8b | 0.0278 | 0.9155 | 0.0% | +0.0278 | Lite |
| smollm2:360m | 0.0274 | 0.6140 | 0.0% | +0.0274 | Lite |
| cogito:3b | 0.0000 | 0.9091 | 0.0% | +0.0000 | Lite |
| falcon3:1b | 0.0000 | 0.3960 | 0.0% | +0.0000 | Lite |
| falcon3:3b | 0.0000 | 0.7867 | 0.0% | +0.0000 | Lite |
| falcon3:7b | 0.0000 | 0.8571 | 0.0% | +0.0000 | Lite |
| gemma3:1b | 0.0000 | 0.5939 | 0.0% | +0.0000 | Lite |
| hermes3:3b | 0.0000 | 0.4222 | 0.0% | +0.0000 | Lite |
| llama3.2:3b | 0.0000 | 0.8075 | 0.0% | +0.0000 | Lite |
| ministral-3:3b | 0.0000 | 0.8936 | 0.0% | +0.0000 | Lite |
| olmo2:7b | 0.0000 | 0.7760 | 0.0% | +0.0000 | Lite |
| shieldgemma:2b | 0.0000 | 0.0000 | 0.0% | +0.0000 | Tie |
| shieldgemma:9b | 0.0000 | 0.0000 | 0.0% | +0.0000 | Tie |

## 📈 Detailed Performance Metrics

### gpt-oss:20b

**Full Prompt:**
- F1=0.9714, Accuracy=0.9689, Precision=0.9855, Recall=0.9577
- Avg Time: 0.84s, Errors: 0

**Lite Prompt:**
- F1=0.9635, Accuracy=0.9689, Precision=1.0000, Recall=0.9296
- Avg Time: 0.90s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.00s, Errors: 71

### gemma3n:e4b

**Full Prompt:**
- F1=0.9403, Accuracy=0.9503, Precision=1.0000, Recall=0.8873
- Avg Time: 0.35s, Errors: 0

**Lite Prompt:**
- F1=0.9559, Accuracy=0.9627, Precision=1.0000, Recall=0.9155
- Avg Time: 0.32s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.97s, Errors: 71

### gemma4:e4b

**Full Prompt:**
- F1=0.9028, Accuracy=0.9130, Precision=0.8904, Recall=0.9155
- Avg Time: 3.10s, Errors: 0

**Lite Prompt:**
- F1=0.9784, Accuracy=0.9814, Precision=1.0000, Recall=0.9577
- Avg Time: 2.71s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 4.54s, Errors: 71

### ministral-3:8b

**Full Prompt:**
- F1=0.8906, Accuracy=0.9130, Precision=1.0000, Recall=0.8028
- Avg Time: 0.24s, Errors: 0

**Lite Prompt:**
- F1=0.9252, Accuracy=0.9317, Precision=0.8947, Recall=0.9577
- Avg Time: 0.19s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 4.15s, Errors: 71

### gemma3:4b

**Full Prompt:**
- F1=0.8732, Accuracy=0.8882, Precision=0.8732, Recall=0.8732
- Avg Time: 0.36s, Errors: 0

**Lite Prompt:**
- F1=0.9079, Accuracy=0.9130, Precision=0.8519, Recall=0.9718
- Avg Time: 0.34s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.91s, Errors: 71

### qwen3:8b

**Full Prompt:**
- F1=0.8640, Accuracy=0.8944, Precision=1.0000, Recall=0.7606
- Avg Time: 2.36s, Errors: 0

**Lite Prompt:**
- F1=0.9160, Accuracy=0.9317, Precision=1.0000, Recall=0.8451
- Avg Time: 1.78s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 3.77s, Errors: 71

### granite4.1:8b

**Full Prompt:**
- F1=0.8099, Accuracy=0.8571, Precision=0.9800, Recall=0.6901
- Avg Time: 0.19s, Errors: 0

**Lite Prompt:**
- F1=0.9565, Accuracy=0.9627, Precision=0.9851, Recall=0.9296
- Avg Time: 0.11s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.82s, Errors: 71

### deepseek-r1:8b

**Full Prompt:**
- F1=0.7931, Accuracy=0.8447, Precision=1.0000, Recall=0.6571
- Avg Time: 2.12s, Errors: 0

**Lite Prompt:**
- F1=0.9323, Accuracy=0.9441, Precision=1.0000, Recall=0.8732
- Avg Time: 1.98s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 4.01s, Errors: 71

### lfm2.5:8b

**Full Prompt:**
- F1=0.6379, Accuracy=0.7391, Precision=0.8222, Recall=0.5211
- Avg Time: 0.94s, Errors: 0

**Lite Prompt:**
- F1=0.7368, Accuracy=0.8137, Precision=0.9767, Recall=0.5915
- Avg Time: 0.72s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.29s, Errors: 71

### mistral:7b

**Full Prompt:**
- F1=0.6286, Accuracy=0.7578, Precision=0.9706, Recall=0.4648
- Avg Time: 0.13s, Errors: 0

**Lite Prompt:**
- F1=0.8571, Accuracy=0.8882, Precision=0.9818, Recall=0.7606
- Avg Time: 0.11s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.51s, Errors: 71

### smallthinker:3b

**Full Prompt:**
- F1=0.6226, Accuracy=0.7516, Precision=0.9429, Recall=0.4648
- Avg Time: 2.16s, Errors: 0

**Lite Prompt:**
- F1=0.5918, Accuracy=0.7267, Precision=0.9355, Recall=0.4328
- Avg Time: 2.20s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.74s, Errors: 71

### cogito:8b

**Full Prompt:**
- F1=0.6154, Accuracy=0.7516, Precision=0.9697, Recall=0.4507
- Avg Time: 0.20s, Errors: 0

**Lite Prompt:**
- F1=0.9007, Accuracy=0.9068, Precision=0.8500, Recall=0.9577
- Avg Time: 0.18s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.93s, Errors: 71

### gemma3:270m

**Full Prompt:**
- F1=0.6121, Accuracy=0.4410, Precision=0.4410, Recall=1.0000
- Avg Time: 0.19s, Errors: 0

**Lite Prompt:**
- F1=0.6244, Accuracy=0.4783, Precision=0.4600, Recall=0.9718
- Avg Time: 0.17s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.30s, Errors: 71

### smollm2:135m

**Full Prompt:**
- F1=0.6118, Accuracy=0.2733, Precision=0.5417, Recall=0.7027
- Avg Time: 0.47s, Errors: 0

**Lite Prompt:**
- F1=0.5683, Accuracy=0.4658, Precision=0.4522, Recall=0.7647
- Avg Time: 0.09s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.25s, Errors: 71

### smollm2:1.7b

**Full Prompt:**
- F1=0.6061, Accuracy=0.4348, Precision=0.4375, Recall=0.9859
- Avg Time: 1.82s, Errors: 0

**Lite Prompt:**
- F1=0.5517, Accuracy=0.5155, Precision=0.4660, Recall=0.6761
- Avg Time: 0.12s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.54s, Errors: 71

### llama3.2:1b

**Full Prompt:**
- F1=0.5939, Accuracy=0.4224, Precision=0.4304, Recall=0.9577
- Avg Time: 1.42s, Errors: 0

**Lite Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.16s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.57s, Errors: 71

### qwen3.5:9b

**Full Prompt:**
- F1=0.5440, Accuracy=0.6335, Precision=0.6071, Recall=0.4928
- Avg Time: 4.58s, Errors: 0

**Lite Prompt:**
- F1=0.8872, Accuracy=0.9068, Precision=0.9516, Recall=0.8310
- Avg Time: 4.16s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 5.23s, Errors: 71

### phi4:14b

**Full Prompt:**
- F1=0.4565, Accuracy=0.6894, Precision=1.0000, Recall=0.2958
- Avg Time: 1.40s, Errors: 0

**Lite Prompt:**
- F1=0.9635, Accuracy=0.9689, Precision=1.0000, Recall=0.9296
- Avg Time: 0.13s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.78s, Errors: 71

### deepseek-r1:1.5b

**Full Prompt:**
- F1=0.4118, Accuracy=0.6149, Precision=0.6364, Recall=0.3043
- Avg Time: 0.99s, Errors: 0

**Lite Prompt:**
- F1=0.3932, Accuracy=0.5590, Precision=0.5000, Recall=0.3239
- Avg Time: 0.99s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.63s, Errors: 71

### granite4.1:3b

**Full Prompt:**
- F1=0.3678, Accuracy=0.6584, Precision=1.0000, Recall=0.2254
- Avg Time: 0.13s, Errors: 0

**Lite Prompt:**
- F1=0.8264, Accuracy=0.8696, Precision=1.0000, Recall=0.7042
- Avg Time: 0.11s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.67s, Errors: 71

### qwen3.5:0.8b

**Full Prompt:**
- F1=0.1690, Accuracy=0.4161, Precision=0.3333, Recall=0.1132
- Avg Time: 1.62s, Errors: 0

**Lite Prompt:**
- F1=0.1429, Accuracy=0.5528, Precision=0.4615, Recall=0.0845
- Avg Time: 1.58s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.66s, Errors: 71

### granite4:350m

**Full Prompt:**
- F1=0.0548, Accuracy=0.5714, Precision=1.0000, Recall=0.0282
- Avg Time: 0.12s, Errors: 0

**Lite Prompt:**
- F1=0.6121, Accuracy=0.4410, Precision=0.4410, Recall=1.0000
- Avg Time: 0.11s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.22s, Errors: 71

### hermes3:8b

**Full Prompt:**
- F1=0.0278, Accuracy=0.5652, Precision=1.0000, Recall=0.0141
- Avg Time: 0.19s, Errors: 0

**Lite Prompt:**
- F1=0.9155, Accuracy=0.9255, Precision=0.9155, Recall=0.9155
- Avg Time: 0.17s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.17s, Errors: 71

### smollm2:360m

**Full Prompt:**
- F1=0.0274, Accuracy=0.5590, Precision=0.5000, Recall=0.0141
- Avg Time: 1.04s, Errors: 0

**Lite Prompt:**
- F1=0.6140, Accuracy=0.4348, Precision=0.4430, Recall=1.0000
- Avg Time: 0.08s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.34s, Errors: 71

### cogito:3b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.19s, Errors: 0

**Lite Prompt:**
- F1=0.9091, Accuracy=0.9193, Precision=0.9028, Recall=0.9155
- Avg Time: 0.17s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.57s, Errors: 71

### falcon3:1b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.15s, Errors: 0

**Lite Prompt:**
- F1=0.3960, Accuracy=0.5776, Precision=0.5405, Recall=0.3125
- Avg Time: 0.14s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.49s, Errors: 71

### falcon3:3b

**Full Prompt:**
- F1=0.0000, Accuracy=0.4161, Precision=0.0000, Recall=0.0000
- Avg Time: 0.14s, Errors: 0

**Lite Prompt:**
- F1=0.7867, Accuracy=0.8012, Precision=0.7468, Recall=0.8310
- Avg Time: 0.13s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.41s, Errors: 71

### falcon3:7b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.15s, Errors: 0

**Lite Prompt:**
- F1=0.8571, Accuracy=0.8882, Precision=0.9818, Recall=0.7606
- Avg Time: 0.14s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.93s, Errors: 71

### gemma3:1b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.38s, Errors: 0

**Lite Prompt:**
- F1=0.5939, Accuracy=0.4224, Precision=0.4304, Recall=0.9577
- Avg Time: 0.37s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.55s, Errors: 71

### hermes3:3b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.18s, Errors: 0

**Lite Prompt:**
- F1=0.4222, Accuracy=0.6584, Precision=1.0000, Recall=0.2676
- Avg Time: 0.19s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.91s, Errors: 71

### llama3.2:3b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.26s, Errors: 0

**Lite Prompt:**
- F1=0.8075, Accuracy=0.8075, Precision=0.7222, Recall=0.9155
- Avg Time: 0.26s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.00s, Errors: 71

### ministral-3:3b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.20s, Errors: 0

**Lite Prompt:**
- F1=0.8936, Accuracy=0.9068, Precision=0.9000, Recall=0.8873
- Avg Time: 0.19s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 2.08s, Errors: 71

### olmo2:7b

**Full Prompt:**
- F1=0.0000, Accuracy=0.5590, Precision=0.0000, Recall=0.0000
- Avg Time: 0.14s, Errors: 0

**Lite Prompt:**
- F1=0.7760, Accuracy=0.7453, Precision=0.6339, Recall=1.0000
- Avg Time: 0.11s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 1.01s, Errors: 71

### shieldgemma:2b

**Full Prompt:**
- F1=0.0000, Accuracy=0.0000, Precision=0.0000, Recall=0.0000
- Avg Time: 0.21s, Errors: 0

**Lite Prompt:**
- F1=0.0000, Accuracy=0.0000, Precision=0.0000, Recall=0.0000
- Avg Time: 0.21s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.18s, Errors: 71

### shieldgemma:9b

**Full Prompt:**
- F1=0.0000, Accuracy=0.0000, Precision=0.0000, Recall=0.0000
- Avg Time: 0.40s, Errors: 0

**Lite Prompt:**
- F1=0.0000, Accuracy=0.0000, Precision=0.0000, Recall=0.0000
- Avg Time: 0.40s, Errors: 0

**No Prompt (Raw):**
- Resistance Rate: 0.0% (0/71 attacks resisted)
- Avg Time: 0.39s, Errors: 71

## 🎓 Conclusions

### Does the prompt make a difference?

- **24/35** models showed significant improvement (>10%) with prompting
- **Strong evidence** that prompting significantly improves classification (avg gain: 0.5847)

### Full vs Lite Prompt

- **Lite prompt is surprisingly effective** (26 wins vs 7)