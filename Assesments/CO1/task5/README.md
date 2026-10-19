# Task 5 – Perform Asymptotic Analysis

## Problem

Asymptotic analysis is used to compare the growth rates of Linear Search, Binary Search, and Hash-Based Search as the number of student registration records increases. The notations Big O (O), Big Omega (Ω), and Big Theta (Θ) describe the upper bound, lower bound, and tight bound of an algorithm's growth rate, respectively.

## Approach 1: Iterative Linear Search

**Time Complexity:** Θ(n) in the average and worst cases.

Linear search checks registration numbers sequentially. In the best case, the target is the first element, requiring one comparison. Therefore, the best-case complexity is Θ(1). In the worst case, all n records must be examined, resulting in Θ(n).

For an average successful search, assuming the target is equally likely to occur at any position:

T_avg(n) = (n + 1) / 2

As n becomes very large, the constant factor 1/2 becomes insignificant in asymptotic analysis. Therefore, the average growth rate is Θ(n).

**Interpretation:** When the dataset increases from 1,000 to 1,000,000 records, the worst-case number of comparisons increases from 1,000 to 1,000,000. Thus, the work increases approximately 1,000 times.

## Approach 2: Binary Search

**Time Complexity:** Θ(log n) in the average and worst cases, assuming the list is sorted.

Binary search divides the search space into two halves after each comparison. Its worst-case number of comparisons is approximately:

T(n) = floor(log₂ n) + 1

For n = 1,000:

log₂(1,000) ≈ 9.97

Therefore, approximately 10 comparisons are sufficient.

For n = 1,000,000:

log₂(1,000,000) ≈ 19.93

Therefore, approximately 20 comparisons are sufficient.

The best case is Θ(1), when the target is the middle element.

**Interpretation:** When the dataset grows from 1,000 to 1,000,000 records, binary search requires only about 10 additional comparisons in the worst case. This makes it highly efficient for large, sorted registration-number datasets. If sorting is required, its preprocessing cost must also be considered.

## Approach 3: Hash-Based Search

**Time Complexity:** Expected Θ(1) for searching and worst-case O(n) under severe collisions.

Hash-based search uses a hash function to calculate the location of a registration number in a hash table. Under suitable hashing and a controlled load factor, the expected number of operations remains approximately constant.

Therefore:

T_avg(n) = Θ(1)

In the best case, the target is found directly at the calculated location, giving Θ(1). In the worst case, many collisions may force the algorithm to examine up to n entries, giving O(n).

Building the hash table requires expected Θ(n) time.

**Interpretation:** Increasing the dataset from 1,000 to 1,000,000 records does not necessarily increase the expected number of operations for a single hash-table search, provided the table is appropriately sized. However, the table construction cost and memory requirements increase with the number of records.

## Comparison of Asymptotic Growth

| Algorithm | Best Case | Average Case | Worst Case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash-Based Search | Θ(1) | Expected Θ(1) | O(n) |

## Conclusion

Asymptotic analysis shows that Linear Search has linear growth, Binary Search has logarithmic growth, and Hash-Based Search has expected constant-time search performance under suitable conditions. For datasets containing more than one million student registration records, Binary Search is efficient when the records are sorted, while Hash-Based Search is suitable for frequent lookups when sufficient memory is available. Linear Search is simpler but becomes less efficient as the dataset grows. Preprocessing costs must be included when comparing algorithms that require sorting or hash-table construction.
