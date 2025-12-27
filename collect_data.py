from core.decision_flow import run_reflection
from core.export import export_profiles

profiles = []

print("Enter decisions (type 'done' to finish):")
while True:
    decision = input("> ")
    if decision.lower() == "done":
        break

    result = run_reflection(decision)
    profiles.append(result.profile)

export_profiles(profiles, "decision_fragility.csv")
print("Saved decision_fragility.csv")
