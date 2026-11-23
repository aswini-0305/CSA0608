"""
CO5 Task B1: Instrumented Graph Colouring
Two selection strategies:
  1. Input order
  2. Dynamic highest-saturation, then highest-degree (DSATUR-style) order
Run: python graph_colouring.py
"""

from dataclasses import dataclass, field

@dataclass
class Stats:
    nodes: int = 0
    attempts: int = 0
    rejected: int = 0
    backtracks: int = 0
    max_depth: int = 0

def graph_colour(adjacency, m, heuristic=False):
    n = len(adjacency)
    colour = [-1] * n
    stats = Stats()

    def choose_vertex():
        uncoloured = [v for v in range(n) if colour[v] == -1]
        if not uncoloured:
            return None
        if not heuristic:
            return uncoloured[0]

        # Prefer the vertex adjacent to the largest number of distinct
        # already-used colours; break ties by degree, then vertex index.
        def priority(v):
            saturation = len({colour[u] for u in adjacency[v] if colour[u] != -1})
            return (saturation, len(adjacency[v]), -v)
        return max(uncoloured, key=priority)

    def search(depth):
        stats.nodes += 1
        stats.max_depth = max(stats.max_depth, depth)
        v = choose_vertex()
        if v is None:
            return True

        for c in range(m):
            stats.attempts += 1
            if all(colour[u] != c for u in adjacency[v]):
                colour[v] = c
                if search(depth + 1):
                    return True
                colour[v] = -1             # undo assignment
                stats.backtracks += 1
            else:
                stats.rejected += 1
        return False

    success = search(0)
    return success, (colour[:] if success else None), stats

def run_case(name, adjacency, m):
    print(f"\n{name} | vertices={len(adjacency)}, colours={m}")
    for heuristic, label in [(False, "Version 1 - Input order"),
                             (True, "Version 2 - DSATUR-style order")]:
        ok, colouring, s = graph_colour(adjacency, m, heuristic)
        print(label)
        print("  Result:", "COLOURABLE" if ok else "NOT COLOURABLE")
        print("  Colouring:", colouring)
        print(f"  Nodes={s.nodes}, Attempts={s.attempts}, "
              f"Rejected={s.rejected}, Backtracks={s.backtracks}, "
              f"MaxDepth={s.max_depth}")

if __name__ == "__main__":
    # Colourable: triangle plus two connected tail vertices; 3 colours.
    colourable = [
        {1, 2}, {0, 2, 3}, {0, 1, 4}, {1, 4}, {2, 3}
    ]
    # Not colourable: complete graph K4 with only 3 colours.
    impossible = [{1,2,3}, {0,2,3}, {0,1,3}, {0,1,2}]
    # Boundary case: empty graph (no conflicts), including one vertex.
    boundary = [set()]
    run_case("Test 1: Colourable graph", colourable, 3)
    run_case("Test 2: K4 with three colours", impossible, 3)
    run_case("Test 3: Single isolated vertex", boundary, 1)
