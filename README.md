# Comparative Opinion Mining for Arabic Social Media

## Overview

This project presents an end-to-end **Comparative Opinion Mining System** for Arabic social media text.

The system performs two main Natural Language Processing (NLP) tasks:

1. **Comparison Detection**
   - Determines whether a sentence contains a comparative opinion.

2. **Named Entity Recognition (NER)**
   - Extracts the entities (brands/products) involved in the comparison.

### Example

**Input**

```text
سامسونج أفضل من ايفون بمراحل
```

**Output**

```json
{
  "classification": 1,
  "entities": ["سامسونج", "ايفون"]
}
```

---

## Project Pipeline

### Phase 1 — Data Preprocessing

- Arabic text cleaning
- Text normalization
- URL removal
- Mention removal
- Emoji removal
- Punctuation handling
- Dataset preparation

### Phase 2 — Comparison Detection

The following approaches were implemented and evaluated:

- TF-IDF + SVM
- BiLSTM + FastText
- AraBERT Classification
- Qwen Few-Shot Prompting

### Phase 3 — Named Entity Recognition

- AraBERT Token Classification

### Phase 4 — Engineering & Deployment

- Model serialization
- API testing
- Docker containerization

---

## Model Performance

### Comparison Detection Results

| Model             | Accuracy   | Precision  | Recall | F1 Score   |
| ----------------- | ---------- | ---------- | ------ | ---------- |
| TF-IDF + SVM      | 0.9047     | 0.8380     | 0.9819 | 0.9043     |
| BiLSTM + FastText | 0.9019     | 0.8238     | 1.0000 | 0.9034     |
| AraBERT           | **0.9102** | **0.8638** | 0.9548 | **0.9070** |
| Qwen Few-Shot     | 0.8191     | 0.8131     | 0.7861 | 0.7994     |

### Named Entity Recognition Results

| Metric    | Score  |
| --------- | ------ |
| Precision | 0.8457 |
| Recall    | 0.8570 |
| F1 Score  | 0.8513 |

---

## Final Selected Models

### Comparison Detection

- AraBERT Classification

### Named Entity Recognition

- AraBERT Token Classification

Detailed evaluation results are available in:

```text
reports/model_report.md
```

---

## Repository Structure

```text
arabic-comparative-opinion-mining/
│
├── app.py
├── requirements.txt
├── requirements-api.txt
├── Dockerfile
├── README.md
│
├── notebooks/
│   ├── 01_Preprocessing.ipynb
│   └── 02_Comparative_Opinion_Mining.ipynb
│
└── reports/
    └── model_report.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<username>/arabic-comparative-opinion-mining.git
cd arabic-comparative-opinion-mining
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

API will be available at:

```text
http://localhost:8000
```

---

## API Endpoints

### Health Check

Request:

```http
GET /
```

Response:

```json
{
  "status": "running"
}
```

---

### Prediction Endpoint

Request:

```http
POST /predict
```

Body:

```json
{
  "text": "سامسونج أفضل من ايفون"
}
```

Response:

```json
{
  "classification": 1,
  "entities": ["سامسونج", "ايفون"]
}
```

---

## Docker

Build the image:

```bash
docker build -t comparative-opinion-mining .
```

Run the container:

```bash
docker run -p 8000:8000 comparative-opinion-mining
```

The API will be available at:

```text
http://localhost:8000
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- TensorFlow
- PyTorch
- Transformers
- AraBERT
- FastAPI
- Docker

---

## Pretrained Models

The trained model weights are not included in this repository due to GitHub file size limitations.

Excluded model directories:

```text
comparison_model/
ner_model/
```

The repository contains all source code, notebooks, deployment files, and documentation required to reproduce the project.

---

## Repository Contents

- Data preprocessing pipeline
- Comparison detection models
- Named entity recognition model
- Evaluation reports
- FastAPI deployment
- Docker configuration
- Experimental notebooks

---

## Author

Malek Magdi

# Comparative Opinion Mining for Arabic Social Media

# Comparative Opinion Mining for Arabic Social Media

## Overview

This project presents an end-to-end **Comparative Opinion Mining System** for Arabic social media text.

The system performs two core Natural Language Processing (NLP) tasks:

1. **Comparison Detection**
   - Determines whether a sentence contains a comparative opinion.

2. **Named Entity Recognition (NER)**
   - Extracts the entities (brands/products) involved in the comparison.

### Example

Input:

```text
سامسونج أفضل من ايفون بمراحل
```

Output:

```json
{
  "classification": 1,
  "entities": ["سامسونج", "ايفون"]
}
```

---

## Project Pipeline

### Phase 1 — Data Preprocessing

- Arabic text cleaning
- Text normalization
- URL removal
- Mention removal
- Emoji removal
- Punctuation handling
- Dataset preparation

### Phase 2 — Comparison Detection

The following approaches were implemented and evaluated:

- TF-IDF + SVM
- BiLSTM + FastText
- AraBERT Classification
- Qwen Few-Shot Prompting

### Phase 3 — Named Entity Recognition

- AraBERT Token Classification

### Phase 4 — Engineering & Deployment

- FastAPI deployment
- API testing
- Docker containerization

---

## Model Performance

### Comparison Detection Results

| Model             | Accuracy   | Precision  | Recall | F1 Score   |
| ----------------- | ---------- | ---------- | ------ | ---------- |
| TF-IDF + SVM      | 0.9047     | 0.8380     | 0.9819 | 0.9043     |
| BiLSTM + FastText | 0.9019     | 0.8238     | 1.0000 | 0.9034     |
| AraBERT           | **0.9102** | **0.8638** | 0.9548 | **0.9070** |
| Qwen Few-Shot     | 0.8191     | 0.8131     | 0.7861 | 0.7994     |

### Named Entity Recognition Results

| Metric    | Score  |
| --------- | ------ |
| Precision | 0.8457 |
| Recall    | 0.8570 |
| F1 Score  | 0.8513 |

---

## Final Selected Models

### Comparison Detection

- AraBERT Classification

### Named Entity Recognition

- AraBERT Token Classification

Detailed evaluation results are available in:

```text
reports/model_report.md
```

---

## Repository Structure

```text
arabic-comparative-opinion-mining/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── notebooks/
│   ├── 1_Preprocessing.ipynb
│   └── 2_Comparative_Opinion_Mining.ipynb
│
└── reports/
    └── model_report.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/MalekMagdi20/arabic-comparative-opinion-mining.git
cd arabic-comparative-opinion-mining
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

---

## API Endpoints

### Health Check

**Request**

```http
GET /
```

**Response**

```json
{
  "status": "running"
}
```

### Prediction Endpoint

**Request**

```http
POST /predict
```

**Body**

```json
{
  "text": "سامسونج أفضل من ايفون"
}
```

**Response**

```json
{
  "classification": 1,
  "entities": ["سامسونج", "ايفون"]
}
```

---

## Docker

Build the image:

```bash
docker build -t comparative-opinion-mining .
```

Run the container:

```bash
docker run -p 8000:8000 comparative-opinion-mining
```

The API will be available at:

```text
http://localhost:8000
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- TensorFlow
- PyTorch
- Transformers
- AraBERT
- FastAPI
- Docker

---

## Pretrained Models

The trained model weights are not included in this repository because GitHub does not support storing large model files directly.

Excluded model directories:

```text
comparison_model/
ner_model/
```

The repository contains all source code, notebooks, deployment files, and documentation required to reproduce the project.

---

## Repository Contents

- Data preprocessing pipeline
- Comparison detection models
- Named Entity Recognition model
- Evaluation reports
- FastAPI deployment
- Docker configuration
- Experimental notebooks

---

## Author

**Malek Magdi**

Comparative Opinion Mining for Arabic Social Media
