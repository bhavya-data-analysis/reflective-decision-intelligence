# core/compare.py
from .profile import DecisionProfile


def compare_profiles(before: DecisionProfile, after: DecisionProfile) -> dict:
    """
    Compare two decision states.
    Positive delta = improvement.
    """
    return {
        "fragility_delta": before.fragility - after.fragility,
        "reflection_depth_delta": after.reflection_depth - before.reflection_depth,
    }
