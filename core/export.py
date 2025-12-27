# core/export.py
import csv
from typing import List
from .profile import DecisionProfile


def fragility_to_label(fragility: int) -> str:
    if fragility <= 2:
        return "LOW"
    elif fragility <= 5:
        return "MEDIUM"
    else:
        return "HIGH"


def export_profiles(profiles: List[DecisionProfile], path: str) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["decision_text", "fragility_label"])

        for p in profiles:
            writer.writerow([
                p.decision_text,
                fragility_to_label(p.fragility)
            ])
