"""
CO5 Task B4: Next-Fit bin-packing heuristic.
The next item is placed in the current server if it fits; otherwise a new
server is opened. This is fast and simple, but not always optimal.
Run: python bin_packing.py
"""

def next_fit(workloads, capacity):
    bins = []
    remaining = []
    for item in workloads:
        if item < 0 or item > capacity:
            raise ValueError(f"Workload {item} must be between 0 and capacity {capacity}")
        if not bins or remaining[-1] < item:
            bins.append([item])
            remaining.append(capacity - item)
        else:
            bins[-1].append(item)
            remaining[-1] -= item
    return bins, remaining

def show(label, workloads, capacity):
    bins, remaining = next_fit(workloads, capacity)
    print(f"\n{label}")
    print("Capacity:", capacity)
    print("Workloads:", workloads)
    print("Servers used:", len(bins))
    for i, (items, rem) in enumerate(zip(bins, remaining), 1):
        print(f"Server {i}: workloads={items}, used={sum(items)}, remaining={rem}")

if __name__ == "__main__":
    show("Normal production example", [4, 7, 2, 6, 5, 3, 8, 2], 10)
    # Deliberately awkward arrival order. Reordering into pairs gives 3 servers:
    # (6,4), (6,4), (6,4). Next-Fit on the given order uses 4.
    show("Challenge input - demonstrates non-optimality",
         [6, 6, 4, 4, 6, 4], 10)
