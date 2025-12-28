from collections import defaultdict

def aggregate_attributions(runs):
    """
    runs = list of ReflectionResult
    """
    stats = defaultdict(lambda: {
        "asked": 0,
        "helped": 0,
        "hurt": 0,
        "no_change": 0,
        "avg_delta": 0.0,
    })

    for run in runs:
        for a in run.attributions:
            s = stats[a["intervention_id"]]
            s["asked"] += 1
            s[a["effect"]] += 1
            s["avg_delta"] += a["delta_fragility"]

    for s in stats.values():
        if s["asked"] > 0:
            s["avg_delta"] /= s["asked"]

    return stats
