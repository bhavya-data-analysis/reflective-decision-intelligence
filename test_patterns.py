from core.decision_flow import run_reflection
from core.history import DecisionHistory

history = DecisionHistory()

for i in range(3):
    print(f"\n=== DECISION {i+1} ===")
    result = run_reflection(input("Decision:\n> "))
    history.add(result.profile)

print("\n--- PATTERN SUMMARY ---")
print(history.pattern_summary())

print("\nFragility trend:", history.fragility_trend())
print("Reflection depth trend:", history.reflection_depth_trend())
