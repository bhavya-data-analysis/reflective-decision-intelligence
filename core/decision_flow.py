# core/decision_flow.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Set
from datetime import datetime, timezone

from .prediction import predict_pre_reflection
from .clarity import detect_decision_clarity
from .analysis import detect_flags
from .questions import BASE_QUESTIONS, FOLLOW_UPS, Question
from .triggers import detect_high_stakes
from .scoring import score_reflection
from .profile import DecisionProfile
from .interventions import Intervention


@dataclass
class ReflectionResult:
    decision: str
    clarity: str
    is_high_stakes: bool
    trigger_reasons: List[str]
    answers: Dict[str, str]
    profile: DecisionProfile
    interventions: List[Intervention]
    attributions: List[Dict]


def ask_input(prompt: str) -> str:
    return input(f"{prompt}\n> ").strip()


def _pick_followups(flags, low_spec_cooldown: int) -> List[Question]:
    if flags.irritated:
        return FOLLOW_UPS["irritation"][:1]

    followups: List[Question] = []

    if flags.deflection:
        followups.extend(FOLLOW_UPS["deflection"])
    if flags.overconfidence:
        followups.extend(FOLLOW_UPS["overconfidence"])
    if flags.emotional:
        followups.extend(FOLLOW_UPS["emotional"])

    if flags.low_specificity and low_spec_cooldown <= 0:
        followups.extend(FOLLOW_UPS["low_specificity"])

    return followups


def run_reflection(decision_text: str) -> ReflectionResult:
    recent_harm = {}
    recent_harm = {
  "specificity": True,
  "deflection": False
}
    # --- ML pre-reflection prediction ---
    pre_prediction = predict_pre_reflection(decision_text)

    if pre_prediction:
        msg = f"[ML pre-check] Predicted fragility: {pre_prediction.label}"
        if pre_prediction.confidence is not None:
            msg += f" (conf {pre_prediction.confidence:.2f})"
        print(msg + "\n")

    clarity = detect_decision_clarity(decision_text)
    trigger = detect_high_stakes(decision_text)

    if trigger.is_high_stakes:
        print("\nThis appears to be a high-stake decision.")
        print("Before acting, please reflect on the following:\n")
    else:
        print("\nLet’s do a quick reflection.\n")

    answers: Dict[str, str] = {}
    interventions_asked: List[Intervention] = []
    intervention_attributions: List[Dict] = []

    total_fragility = 0
    total_depth = 0
    all_signals: Dict[str, int] = {}

    asked_followup_keys: Set[str] = set()
    low_spec_cooldown = 0

    for q in BASE_QUESTIONS:
        ans = ask_input(q.prompt)
        answers[q.key] = ans

        flags = detect_flags(ans)
        score = score_reflection(
            flags=flags,
            answer_text=ans,
            is_high_stakes=trigger.is_high_stakes,
        )

        total_fragility += score.decision_fragility
        total_depth += score.reflection_depth

        for k, v in score.signals.items():
            all_signals[k] = all_signals.get(k, 0) + v

        followups = _pick_followups(flags, low_spec_cooldown)

        asked = 0
        for fq in followups:
            if asked >= 2 or fq.key in asked_followup_keys:
                continue

            # --- intervention begins ---
            intervention = Intervention(
                id=fq.key,
                type="followups",
                target_failure=fq.key,
                cognitive_state_before=clarity.level.value,
                question_text=fq.prompt,
                timestamp=datetime.now(timezone.utc),
            )
            #-- Level 4.3 -
            if recent_harm.get(intervention.type):
                continue

            interventions_asked.append(intervention)

            fragility_before = total_fragility
            # ask the question

            f_ans = ask_input(intervention.question_text)
            answers[fq.key] = f_ans

#score followup
            f_flags = detect_flags(f_ans)
            f_score = score_reflection(
                flags=f_flags,
                answer_text=f_ans,
                is_high_stakes=trigger.is_high_stakes,
            )

            total_fragility += f_score.decision_fragility
            total_depth += f_score.reflection_depth

            for k, v in f_score.signals.items():
                all_signals[k] = all_signals.get(k, 0) + v

            delta = fragility_before - total_fragility

            intervention_attributions.append({
                "intervention_id": intervention.id,
                "delta_fragility": delta,
                "effect": (
                    "helped" if delta > 0
                    else "hurt" if delta < 0
                    else "no_change"
                ),
            })

            asked_followup_keys.add(fq.key)
            asked += 1

            if "specific" in fq.key.lower():
                low_spec_cooldown = 2

        low_spec_cooldown = max(0, low_spec_cooldown - 1)

    # --- reflection effect (overall ML vs rules) ---
    reflection_effect = None
    if pre_prediction:
        ml_level = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}.get(pre_prediction.label)
        rule_level = 1 if total_fragility <= 2 else 2 if total_fragility <= 5 else 3

        if rule_level < ml_level:
            reflection_effect = "helped"
        elif rule_level > ml_level:
            reflection_effect = "hurt"
        else:
            reflection_effect = "no_change"

    profile = DecisionProfile(
        decision_text=decision_text,
        clarity=clarity.level.value,
        fragility=total_fragility,
        reflection_depth=total_depth,
        signals=all_signals,
        reflection_effect=reflection_effect,
    )

    return ReflectionResult(
        decision=decision_text,
        clarity=clarity.level.value,
        is_high_stakes=trigger.is_high_stakes,
        trigger_reasons=trigger.reasons,
        answers=answers,
        profile=profile,
        interventions=interventions_asked,
        attributions=intervention_attributions,
    )
