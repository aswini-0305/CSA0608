"""
CO5 Task B2: Same-size graph instances with different search behaviour.
Graph A is a path (easy); Graph B contains K4 (not 3-colourable).
Both have 8 vertices and use m=3.
Run: python adversarial_graphs.py
"""
from dataclasses import dataclass

@dataclass
class Stats:
    nodes: int = 0
    attempts: int = 0
    rejected: int = 0
    backtracks: int = 0
    max_depth: int = 0

def solve(adj, m):
    n = len(adj)
    colours = [-1] * n
    st = Stats()

    def dfs(v, depth):
        st.nodes += 1
        st.max_depth = max(st.max_depth, depth)
        if v == n:
            return True
        for c in range(m):
            st.attempts += 1
            if any(colours[u] == c for u in adj[v]):
                st.rejected += 1
                continue
            colours[v] = c
            if dfs(v + 1, depth + 1):
                return True
            colours[v] = -1
            st.backtracks += 1
        return False

    ok = dfs(0, 0)
    return ok, colours if ok else None, st

def make_path(n):
    adj = [set() for _ in range(n)]
    for v in range(n - 1):
        adj[v].add(v + 1)
        adj[v + 1].add(v)
    return adj

def make_k4_plus_isolates(n):
    adj = [set() for _ in range(n)]
    for u in range(4):
        for v in range(u + 1, 4):
            adj[u].add(v)
            adj[v].add(u)
    return adj

if __name__ == "__main__":
    cases = [
        ("Graph A - Path graph (easy)", make_path(8)),
        ("Graph B - K4 plus four isolated vertices (harder)", make_k4_plus_isolates(8))
    ]
    for name, graph in cases:
        ok, col, s = solve(graph, 3)
        print("\n" + name)
        print("Vertices=8, Colours=3")
        print("Result:", "COLOURABLE" if ok else "NOT COLOURABLE")
        print("Colouring:", col)
        print(f"Nodes={s.nodes}, Attempts={s.attempts}, "
              f"Rejected={s.rejected}, Backtracks={s.backtracks}")
