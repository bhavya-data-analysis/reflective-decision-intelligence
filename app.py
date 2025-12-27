# app.py
from __future__ import annotations

from core.decision_flow import run_reflection


def main() -> None:
    print("Reflective Decision Intelligence — Career Decisions\n")
    decision = input("What decision are you considering?\n> ").strip()

    result = run_reflection(decision)

    print("\n--- Reflection Summary ---")
    print(f"Decision: {result.decision}")
    print("High-stakes: Yes" if result.is_high_stakes else "High-stakes: No")

    if result.trigger_reasons:
        print("Triggers:", "; ".join(result.trigger_reasons))

    for k, v in result.answers.items():
        print(f"{k.capitalize()}: {v}")

    print("\nTake time to consider this before acting.")


if __name__ == "__main__":
    main()
