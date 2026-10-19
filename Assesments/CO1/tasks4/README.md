# Task 4 – Analyse Best, Average and Worst-Case Behaviour

## Problem

The performance of Linear Search, Binary Search, and Hash-Based Search is analysed under different input conditions. The best case represents the minimum number of operations, the average case represents the expected number of operations, and the worst case represents the maximum number of operations for a given input size.

## Approach 1: Iterative Linear Search

**Basic Operation:** Comparing the target registration number with an element in the list.

### Best Case

The best case occurs when the target registration number is the first element in the list. The algorithm finds the target immediately and performs only one comparison.

Number of comparisons = 1

T_best(n) = 1

Therefore, the best-case time complexity is O(1).

### Average Case

The average case occurs when the target is equally likely to appear at any position in the list. If the target is present, it may require 1, 2, 3, ..., n comparisons.

Average number of comparisons:

T_avg(n) = (1 + 2 + 3 + ... + n) / n

T_avg(n) = n(n + 1) / 2n

T_avg(n) = (n + 1) / 2

Therefore, the average-case time complexity is O(n).

### Worst Case

The worst case occurs when the target is the last element or is not present in the list. The algorithm must check every element before terminating.

Number of comparisons = n

T_worst(n) = n

Therefore, the worst-case time complexity is O(n).

### Explanation

The number of comparisons depends on the position of the target. If it appears near the beginning, fewer comparisons are needed. If it appears at the end or is absent, all n elements must be examined.

## Approach 2: Binary Search

**Basic Operation:** Comparing the target registration number with the middle element of a sorted list.

### Best Case

The best case occurs when the target registration number is exactly the middle element of the sorted list. The target is found in the first comparison.

Number of comparisons = 1

T_best(n) = 1

Therefore, the best-case time complexity is O(1).

### Average Case

The average case occurs when the target is found after several divisions of the search space. At every step, binary search eliminates approximately half of the remaining
