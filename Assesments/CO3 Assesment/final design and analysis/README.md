# FINAL DESIGN AND ANALYSIS

## 1. INTRODUCTION

The online ordering platform requires efficient algorithms to manage order consolidation, seller score updates, order searching and product recommendations.

Each module has different computational requirements. Therefore, suitable algorithms are selected based on time complexity, memory usage, performance and practical requirements.

The final design combines four algorithms: Merge Sort, Quick Sort, Binary Search and Strassen's Matrix Multiplication.

## 2. FINAL ALGORITHM DESIGN

The following algorithms are selected for the four modules.

| Module | Computational Requirement | Selected Algorithm |
|---|---|---|
| Module 1 – Nightly Order Consolidation | Stable sorting of orders by timestamp | Merge Sort |
| Module 2 – Live Seller Leaderboard | Efficient sorting of nearly sorted seller scores | Quick Sort with Median-of-Three |
| Module 3 – Order Lookup | Finding the first matching timestamp | Modified Binary Search |
| Module 4 – Recommendation Scores | Efficient multiplication of large matrices | Strassen's Algorithm with Hybrid Approach |

## 3. TIME AND SPACE COMPLEXITY ANALYSIS

| Module | Algorithm | Time Complexity | Extra Space |
|---|---|---|---|
| Module 1 | Merge Sort | O(n log n) | O(n) |
| Module 2 | Quick Sort | Average: O(n log n), Worst: O(n²) | Average: O(log n), Worst: O(n) |
| Module 3 | Binary Search | O(log n) | O(1) |
| Module 4 | Strassen's Algorithm | O(n^2.807) | O(n²) auxiliary storage in a straightforward implementation |

## 4. JUSTIFICATION OF ALGORITHM SELECTION

### MODULE 1 – NIGHTLY ORDER CONSOLIDATION

**Selected Algorithm: Merge Sort**

Merge Sort is selected because the platform must sort orders according to timestamps while maintaining the original arrival order of orders with equal timestamps.

Reasons:
1. It is a stable sorting algorithm.
2. It guarantees O(n log n) time complexity.
3. It performs consistently for large datasets.
4. It is suitable for audit report generation.
5. External Merge Sort can handle datasets that do not fit in RAM.

**Main Trade-off:**

Merge Sort requires additional memory for merging.

**Condition for Changing the Algorithm:**

If memory availability becomes extremely limited and stability is not required, an in-place sorting algorithm may be considered.

### MODULE 2 – LIVE SELLER LEADERBOARD

**Selected Algorithm: Quick Sort with Median-of-Three**

Quick Sort is selected because the leaderboard requires frequent score sorting.

Reasons:
1. It provides O(n log n) average-case performance.
2. It uses in-place partitioning.
3. Median-of-Three improves pivot selection.
4. It reduces the likelihood of unbalanced partitions.
5. It is suitable for large collections of seller scores.

**Main Trade-off:**

Quick Sort has O(n²) worst-case time complexity and is not stable.

**Condition for Changing the Algorithm:**

If the leaderboard becomes extremely large and only a few scores change between updates, Insertion Sort or an incremental ordered data structure may be more suitable.

### MODULE 3 – ORDER LOOKUP

**Selected Algorithm: Modified Binary Search**

Binary Search is selected because Module 1 already produces a sorted order list.

Reasons:
1. It searches efficiently in sorted data.
2. It reduces the search area by half in each iteration.
3. It provides O(log n) worst-case time complexity.
4. It uses O(1) extra space in an iterative implementation.
5. The modified version returns the first matching timestamp.

**Main Trade-off:**

Binary Search requires sorted input.

**Condition for Changing the Algorithm:**

If orders are stored in an unsorted collection, or if frequent individual lookups require direct access, a hash table or indexed database structure may be more suitable.

### MODULE 4 – RECOMMENDATION SCORES

**Selected Algorithm: Strassen's Algorithm with Hybrid Approach**

Strassen's algorithm is selected because the platform performs large-scale matrix multiplication to calculate recommendation scores.

Reasons:
1. It uses seven recursive multiplications instead of eight.
2. It provides O(n^2.807) theoretical time complexity.
3. It reduces the number of scalar multiplications.
4. It is suitable for large square matrices.
5. A hybrid approach reduces unnecessary recursion for smaller matrices.

**Main Trade-off:**

It requires additional memory and performs more matrix additions and subtractions.

**Condition for Changing the Algorithm:**

For small matrices, or when memory and numerical precision are major concerns, conventional matrix multiplication may be more suitable.

## 5. PERFORMANCE ANALYSIS

### Module 1 – Merge Sort

Input size = 10,000,000 orders.

Approximate comparison-scale estimate:

n log₂ n

= 10,000,000 × 23.2535

≈ 232,535,000

Merge Sort provides predictable performance and maintains stability.

### Module 2 – Quick Sort

Input size = 100,000 sellers.

Average comparison-scale estimate:

n log₂ n

= 100,000 × 16.6094

≈ 1,660,940

This is an approximate balanced-partition estimate, not a guaranteed comparison count. Median-of-Three improves practical pivot selection.

### Module 3 – Binary Search

Input size = 10,000,000 orders.

Maximum search iterations:

ceil(log₂(10,000,001)) = 24

Therefore, at most 24 loop iterations are required by the modified algorithm.

### Module 4 – Strassen's Algorithm

Input matrix size = 1024 × 1024.

Conventional multiplication:

1024³ = 1,073,741,824 scalar multiplications.

Strassen's multiplication:

7¹⁰ = 282,475,249 scalar multiplications.

Strassen's method theoretically reduces the number of scalar multiplications, although practical execution time depends on memory usage, implementation and hardware.

## 6. OVERALL SYSTEM DESIGN

The four modules work together as follows:

**Step 1: Order Consolidation**

Merge Sort arranges all incoming orders by timestamp and preserves the original arrival order for equal timestamps.

**Step 2: Seller Leaderboard**

Quick Sort arranges seller scores using an improved pivot selection strategy.

**Step 3: Order Lookup**

Modified Binary Search searches the consolidated order list and returns the first matching timestamp.

**Step 4: Recommendation Calculation**

Strassen's algorithm calculates recommendation scores by multiplying the preference matrix and product matrix.

## 7. MAIN TRADE-OFF ANALYSIS

| Module | Main Trade-off |
|---|---|
| Module 1 | Stable sorting versus additional memory |
| Module 2 | Fast average performance versus quadratic worst case |
| Module 3 | Fast searching versus the requirement for sorted data |
| Module 4 | Fewer multiplications versus additional memory and arithmetic overhead |

## 8. FINAL RECOMMENDATION

The selected algorithms are appropriate for the platform because each algorithm addresses a different computational requirement.

Merge Sort provides stable order consolidation. Quick Sort provides efficient average-case leaderboard sorting. Binary Search provides fast order lookup. Strassen's algorithm improves the theoretical efficiency of large recommendation matrix multiplication.

A hybrid approach can further improve practical performance by selecting algorithms according to input size, memory availability and update frequency.

## 9. CONCLUSION

The final algorithmic design combines four different algorithms to improve the overall performance of the online ordering platform.

Each algorithm is selected after considering its time complexity, space complexity, advantages, disadvantages and practical limitations.

The proposed design provides reliable order management, efficient seller ranking, faster order searching and improved recommendation score calculations.

Therefore, the combination of Merge Sort, Quick Sort, Binary Search and Strassen's Matrix Multiplication provides a suitable algorithmic solution for the four modules of the online ordering platform.
