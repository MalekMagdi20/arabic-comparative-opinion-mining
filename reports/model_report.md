# Comparative Opinion Mining System – Model Report

## 1. Project Overview

This project implements an end-to-end Comparative Opinion Mining system for Arabic social media text.

The system performs two main tasks:

1. Comparison Detection (Binary Classification)
2. Entity Extraction (Named Entity Recognition)

The objective is to identify comparative statements and extract the entities participating in the comparison.

---

# 2. Dataset Preparation

A complete preprocessing pipeline was applied to handle noisy social media text.

Preprocessing steps included:

- URL removal
- Mention removal
- Hashtag cleaning
- Emoji removal
- Punctuation removal
- Arabic text normalization
- Whitespace normalization
- Text cleaning and standardization

The cleaned dataset was then used for all classification and NER experiments.

---

# 3. Modeling Approaches

Four different approaches were implemented and benchmarked for comparison detection.

## 3.1 Classical Machine Learning

Architecture:

- TF-IDF Features
- N-gram Features
- Support Vector Machine (SVM)

Purpose:

- Fast baseline model
- Low inference latency
- Strong performance on sparse textual features

---

## 3.2 Deep Learning

Architecture:

- FastText Arabic Embeddings
- Bidirectional LSTM

Purpose:

- Capture contextual information
- Learn sequential patterns in comparative sentences

---

## 3.3 Transformer-Based Model

Architecture:

- AraBERT

Purpose:

- Fine-tuned transformer model for Arabic comparison detection
- Context-aware language understanding

---

## 3.4 Large Language Model

Architecture:

- Qwen Few-Shot Prompting

Purpose:

- Evaluate zero/few-shot capabilities without task-specific fine-tuning

---

## 3.5 Named Entity Recognition

Architecture:

- AraBERT Token Classification

Labels:

- O
- B-BRAND
- I-BRAND

Purpose:

- Extract brands and products participating in comparisons

---

# 4. Classification Results

| Model             | Accuracy | Precision | Recall | F1 Score | Inference Time (ms/sample) |
| ----------------- | -------- | --------- | ------ | -------- | -------------------------- |
| TF-IDF + SVM      | 0.9047   | 0.8380    | 0.9819 | 0.9043   | 0.07                       |
| BiLSTM + FastText | 0.9019   | 0.8238    | 1.0000 | 0.9034   | 0.98                       |
| AraBERT           | 0.9102   | 0.8638    | 0.9548 | 0.9070   | 8.82                       |
| Qwen Few-Shot     | 0.8191   | 0.8131    | 0.7861 | 0.7994   | 1336.23                    |

---

# 5. NER Results

## AraBERT Token Classification

| Metric    | Score  |
| --------- | ------ |
| Precision | 0.8457 |
| Recall    | 0.8570 |
| F1 Score  | 0.8513 |

Detailed Results:

| Entity | Precision | Recall | F1   |
| ------ | --------- | ------ | ---- |
| BRAND  | 0.85      | 0.86   | 0.85 |

---

# 6. Analysis

## Classification Performance

AraBERT achieved the highest overall classification performance:

- Accuracy: 91.02%
- Precision: 86.38%
- Recall: 95.48%
- F1 Score: 90.70%

Although SVM achieved very competitive results, AraBERT consistently produced the strongest balance between precision and recall.

The BiLSTM model achieved perfect recall (100%) but produced lower precision, indicating a higher tendency toward false positives.

Qwen Few-Shot prompting achieved the weakest performance and suffered from extremely high inference latency.

---

## Inference Speed Analysis

Inference speed is critical for production deployment.

| Model             | Time (ms/sample) |
| ----------------- | ---------------- |
| TF-IDF + SVM      | 0.07             |
| BiLSTM + FastText | 0.98             |
| AraBERT           | 8.82             |
| Qwen Few-Shot     | 1336.23          |

Observations:

- SVM is by far the fastest model.
- AraBERT is slower than SVM but still practical for real-time inference.
- Qwen Few-Shot is significantly slower and unsuitable for production deployment in this scenario.

---

# 7. Final Model Selection

## Selected Classification Model

AraBERT was selected as the final comparison detection model.

Reasons:

1. Highest F1 Score (0.9070)
2. Highest overall Accuracy (0.9102)
3. Strong balance between Precision and Recall
4. Robust contextual understanding of Arabic text
5. Acceptable inference latency for deployment

---

## Selected NER Model

AraBERT Token Classification was selected as the final entity extraction model.

Reasons:

1. Strong token-level performance
2. F1 Score of 0.8513
3. Effective extraction of compared brands and products
4. Seamless integration with the classification pipeline

---

# 8. Engineering & Deployment

The final system was deployed using:

- FastAPI
- Transformers
- PyTorch
- Docker

The deployed API exposes:

POST /predict

Input:

```json
{
  "text": "سامسونج أفضل من ايفون"
}
```

Output:

```json
{
  "classification": 1,
  "entities": ["سامسونج", "ايفون"]
}
```

---

# 9. Conclusion

This project successfully implemented an end-to-end Comparative Opinion Mining system for Arabic social media text.

Four classification approaches and one NER model were evaluated.

Among all tested approaches:

- AraBERT achieved the best overall classification performance.
- AraBERT Token Classification achieved strong entity extraction performance.
- FastAPI and Docker were used to transform the notebook-based solution into a production-ready service.

The resulting system can accurately identify comparative sentences and extract the entities involved, making it suitable for social media monitoring, market analysis, and consumer insight applications.
