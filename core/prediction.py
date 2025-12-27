# core/prediction.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class PreReflectionPrediction:
    label: str
    confidence: Optional[float]


def predict_pre_reflection(decision_text: str) -> Optional[PreReflectionPrediction]:
    """
    Thin wrapper around ML.
    Core logic should never know ML internals.
    """
    try:
        from ml_predict import predict_fragility
    except ImportError:
        return None

    label, confidence = predict_fragility(decision_text)

    if label is None:
        return None

    return PreReflectionPrediction(
        label=label,
        confidence=confidence,
    )
