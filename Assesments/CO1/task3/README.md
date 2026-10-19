# Task 3 – Derive the Time-Complexity Function Mathematically

## Problem

Given unique student registration numbers and a target registration number, determine whether the target exists and return its position or record. Derive the mathematical time-complexity function for each proposed searching algorithm, including preprocessing and total costs.

## Approach 1: Iterative Linear Search

**Input size:** n, the number of student registration numbers.

**Basic operation:** Comparing the target registration number with each element.

### Mathematical Derivation

In linear search, elements are checked sequentially from the beginning until the target is found or the list ends.

**Best Case:**

If the target is the first element, only one comparison is required.

T_best(n) = 1

**Worst Case:**

If the target is the last element or absent, all n elements must be checked.

T_worst(n) = 1 + 1 + 1 + ... + 1 (n times)

T_worst(n) = n

**Average Case:**

Assuming the target is equally likely to occur at any position:

T_avg(n) = (1 + 2 + 3 + ... + n) / n

Using the arithmetic series formula:

T_avg(n) = [n(n + 1) / 2] / n

T_avg(n) = (n + 1) / 2

**Preprocessing Cost:** No preprocessing is required, so the cost is O(1).

**Overall Cost:**

T_total(n) = O(1) + O(n)

T_total(n) = O(n)

Therefore, the worst-case time complexity is O(n).

## Approach 2: Binary Search

**Input size:** n, the number of student registration numbers.

**Basic operation:** Comparing the target with the middle element of the sorted list.

### Mathematical Derivation

Binary search divides the search space into two halves after each comparison.

After the first comparison, the remaining elements are approximately n/2.

After the second comparison, the remaining elements are approximately n/4.

After k comparisons, the remaining elements are approximately:

Remaining elements = n / 2^k

The search stops
