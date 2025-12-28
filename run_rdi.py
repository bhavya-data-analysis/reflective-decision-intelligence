from core.decision_flow import run_reflection
from core.aggregation import aggregate_attributions

def get_decision():
    d = input("\nEnter a decision (or 'q' to quit): ").strip()
    if d.lower() in {"q", "quit", "exit"}:
        return None
    return d


all_runs = []

try:
    while True:
        decision = get_decision()
        if decision is None:
            break

        if not decision:
            continue

        result = run_reflection(decision)
        all_runs.append(result)

except KeyboardInterrupt:
    print("\nExiting safely.")

stats = aggregate_attributions(all_runs)

print("\n--- Aggregated Intervention Stats ---")
for k, v in stats.items():
    print(k, v)
