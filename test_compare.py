from core.decision_flow import run_reflection
from core.compare import compare_profiles

print("=== BEFORE REFLECTION ===")
decision = input("Decision:\n> ")
before = run_reflection(decision).profile

print("\n=== AFTER REFLECTION ===")
after = run_reflection(decision).profile

comparison = compare_profiles(before, after)

print("\n--- COMPARISON ---")
print(comparison)
