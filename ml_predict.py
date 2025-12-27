# ml_predict.py
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "models/fragility_model.joblib"
VEC_PATH = "models/fragility_vectorizer.joblib"


def train_and_save(csv_path: str = "decision_fragility.csv") -> None:
    df = pd.read_csv(csv_path)

    X = df["decision_text"].astype(str).fillna("")
    y = df["fragility_label"].astype(str).fillna("")

    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
    )
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_vec, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VEC_PATH)


def predict_fragility(decision_text: str):
    """
    Returns (label, confidence) or (None, None) if model not ready.
    """
    if not (os.path.exists(MODEL_PATH) and os.path.exists(VEC_PATH)):
        return None, None

    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VEC_PATH)

    X_vec = vectorizer.transform([decision_text])
    label = model.predict(X_vec)[0]

    confidence = None
    if hasattr(model, "predict_proba"):
        confidence = float(max(model.predict_proba(X_vec)[0]))

    return label, confidence
