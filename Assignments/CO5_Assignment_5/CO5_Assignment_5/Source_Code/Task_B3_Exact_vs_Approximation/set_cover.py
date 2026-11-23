"""
CO5 Task B3: Exact minimum set cover vs greedy approximation.
Sets are represented as dictionaries: centre name -> zones served.
Run: python set_cover.py
"""
from itertools import combinations

def exact_set_cover(universe, centres):
    names = list(centres)
    checked = 0
    for size in range(1, len(names) + 1):
        for chosen in combinations(names, size):
            checked += 1
            covered = set()
            for name in chosen:
                covered |= centres[name]
            if covered >= universe:
                return list(chosen), checked
    return None, checked

def greedy_set_cover(universe, centres):
    uncovered = set(universe)
    selected = []
    steps = 0
    while uncovered:
        steps += 1
        best = max(centres, key=lambda name: (len(centres[name] & uncovered),
                                               name))
        gain = centres[best] & uncovered
        if not gain:
            return None, steps
        selected.append(best)
        uncovered -= gain
    return selected, steps

def evaluate(label, universe, centres):
    exact, checks = exact_set_cover(universe, centres)
    greedy, steps = greedy_set_cover(universe, centres)
    print(f"\n{label}")
    print("Universe:", sorted(universe))
    print("Centres:", {k: sorted(v) for k, v in centres.items()})
    print("Exact cover:", exact, "| size =", len(exact) if exact else None,
          "| subsets checked =", checks)
    print("Greedy cover:", greedy, "| size =", len(greedy) if greedy else None,
          "| selections =", steps)
    print("Same optimum:", len(exact) == len(greedy) if exact and greedy else False)

if __name__ == "__main__":
    # Three normal instances; the third is deliberately a greedy counterexample.
    evaluate("Instance 1", set("ABC"),
             {"C1": set("AB"), "C2": set("BC"), "C3": set("AC")})
    evaluate("Instance 2", set("ABCDEF"),
             {"C1": set("ABC"), "C2": set("DEF"), "C3": set("AD"),
              "C4": set("BE"), "C5": set("CF")})
    evaluate("Instance 3 - Counterexample", set("123456"),
             {"A": set("1234"), "B": set("125"), "C": set("346"),
              "D": set("5"), "E": set("6")})

    # Larger deterministic instance: instrumentation counts, not only time.
    universe = set(range(1, 13))
    centres = {
        "S1": set(range(1, 5)), "S2": set(range(5, 9)),
        "S3": set(range(9, 13)), "S4": {1,2,5,6,9},
        "S5": {3,4,7,8,11,12}, "S6": {2,4,6,8,10,12},
        "S7": {1,3,5,7,9,11}
    }
    evaluate("Larger instance (12 zones, 7 centres)", universe, centres)
