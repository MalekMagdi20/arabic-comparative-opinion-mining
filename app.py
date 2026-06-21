<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification
)

# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="Comparative Opinion Mining API"
)

# ==========================================
# Load Classification Model
# ==========================================

clf_tokenizer = AutoTokenizer.from_pretrained(
    "comparison_model"
)

clf_model = AutoModelForSequenceClassification.from_pretrained(
    "comparison_model"
)

# ==========================================
# Load NER Model
# ==========================================

ner_tokenizer = AutoTokenizer.from_pretrained(
    "ner_model"
)

ner_model = AutoModelForTokenClassification.from_pretrained(
    "ner_model"
)

# ==========================================
# Label Mapping
# ==========================================

label_map = {
    0: "O",
    1: "B-BRAND",
    2: "I-BRAND"
}

# ==========================================
# Input Schema
# ==========================================

class InputText(BaseModel):
    text: str

# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():

    return {
        "status": "running"
    }

# ==========================================
# Prediction Endpoint
# ==========================================

@app.post("/predict")
def predict(input: InputText):

    # --------------------------
    # Classification
    # --------------------------

    clf_inputs = clf_tokenizer(
        input.text,
        return_tensors="pt",
        truncation=True
    )

    with torch.no_grad():

        clf_outputs = clf_model(
            **clf_inputs
        )

    comparison_label = torch.argmax(
        clf_outputs.logits,
        dim=1
    ).item()

    # --------------------------
    # NER
    # --------------------------

    ner_inputs = ner_tokenizer(
        input.text,
        return_tensors="pt",
        truncation=True
    )

    with torch.no_grad():

        ner_outputs = ner_model(
            **ner_inputs
        )

    ner_predictions = torch.argmax(
        ner_outputs.logits,
        dim=2
    )[0].tolist()

    word_ids = ner_inputs.word_ids()

    original_words = input.text.split()

    entities = []
    used_words = set()

    for pred, word_id in zip(
        ner_predictions,
        word_ids
    ):

        if word_id is None:
            continue

        label = label_map.get(
            pred,
            "O"
        )

        if label != "O":

            if (
                word_id < len(original_words)
                and word_id not in used_words
            ):

                entities.append(
                    original_words[word_id]
                )

                used_words.add(word_id)

    # --------------------------
    # Response
    # --------------------------

    return {
        "classification": comparison_label,
        "entities": entities
=======
from fastapi import FastAPI
from pydantic import BaseModel

import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForTokenClassification
)

# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="Comparative Opinion Mining API"
)

# ==========================================
# Load Classification Model
# ==========================================

clf_tokenizer = AutoTokenizer.from_pretrained(
    "comparison_model"
)

clf_model = AutoModelForSequenceClassification.from_pretrained(
    "comparison_model"
)

# ==========================================
# Load NER Model
# ==========================================

ner_tokenizer = AutoTokenizer.from_pretrained(
    "ner_model"
)

ner_model = AutoModelForTokenClassification.from_pretrained(
    "ner_model"
)

# ==========================================
# Label Mapping
# ==========================================

label_map = {
    0: "O",
    1: "B-BRAND",
    2: "I-BRAND"
}

# ==========================================
# Input Schema
# ==========================================

class InputText(BaseModel):
    text: str

# ==========================================
# Home Endpoint
# ==========================================

@app.get("/")
def home():

    return {
        "status": "running"
    }

# ==========================================
# Prediction Endpoint
# ==========================================

@app.post("/predict")
def predict(input: InputText):

    # --------------------------
    # Classification
    # --------------------------

    clf_inputs = clf_tokenizer(
        input.text,
        return_tensors="pt",
        truncation=True
    )

    with torch.no_grad():

        clf_outputs = clf_model(
            **clf_inputs
        )

    comparison_label = torch.argmax(
        clf_outputs.logits,
        dim=1
    ).item()

    # --------------------------
    # NER
    # --------------------------

    ner_inputs = ner_tokenizer(
        input.text,
        return_tensors="pt",
        truncation=True
    )

    with torch.no_grad():

        ner_outputs = ner_model(
            **ner_inputs
        )

    ner_predictions = torch.argmax(
        ner_outputs.logits,
        dim=2
    )[0].tolist()

    word_ids = ner_inputs.word_ids()

    original_words = input.text.split()

    entities = []
    used_words = set()

    for pred, word_id in zip(
        ner_predictions,
        word_ids
    ):

        if word_id is None:
            continue

        label = label_map.get(
            pred,
            "O"
        )

        if label != "O":

            if (
                word_id < len(original_words)
                and word_id not in used_words
            ):

                entities.append(
                    original_words[word_id]
                )

                used_words.add(word_id)

    # --------------------------
    # Response
    # --------------------------

    return {
        "classification": comparison_label,
        "entities": entities
>>>>>>> e65b3dc7ad11ab02ca25cd97cd70835292385881
    }