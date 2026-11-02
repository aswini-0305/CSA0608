# TASK (d) – ANALYSE BEFORE AND AFTER (10 MARKS)

## 1. Introduction

The SentinelOps SOC Alert-Triage Module is used to sort security alerts, check blocked IP addresses, identify attack signatures in log files and find the closest login locations.

This task analyses the performance of algorithms before and after optimisation. It compares basic operations, time complexity and performance for different input sizes.

## 2. Basic Operations and Time Complexity

| Function | Basic Operation | Before Optimisation | After Optimisation |
|---|---|---|---|
| Insertion Sort | Severity comparison | O(n²) | O(n²) |
| Blocklist Search | IP address comparison | O(n) | O(1) average |
| String Matching | Character comparison | O(nm) | O(nm) |
| Closest Pair | Distance comparison | O(n²) | O(n²) |

## 3. Insertion Sort Analysis

Insertion Sort arranges security alerts according to severity, with the highest severity first.

Before Optimisation:
- The original code uses an incorrect loop condition.
- It does not correctly process the first element.
- Some alerts may not be placed in the correct position.

After Optimisation:
- The loop condition is changed to j >= 0.
- The key is inserted at position j + 1.
- Equal-severity alerts maintain their original arrival order.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n²)
- Worst Case: O(n²)

## 4. Blocklist Search Analysis

Blocklist Search checks whether an IP address is present in the blocked IP list.

Before Optimisation:
- Sequential search checks each IP address one by one.
- It requires O(n) time in the worst case.

After Optimisation:
- A Python set is used to store blocked IP addresses.
- Set membership provides O(1) average lookup time.
- The set is created once and reused for multiple searches.

Time Complexity:
- Before: O(n)
- After: O(1) average lookup, with O(n) initial set construction.

## 5. String Matching Analysis

String Matching identifies all occurrences of an attack signature in a log file.

Before Optimisation:
- The original loop does not check the final possible starting position.
- It has an incorrect matching condition.
- This may produce missing or incorrect results.

After Optimisation:
- The loop checks positions from 0 to n-m.
- The matching process stops when a character does not match.
- Every valid occurrence is recorded.

Time Complexity:
- Before: O(nm)
- After: O(nm)

Where:
- n = Length of the log.
- m = Length of the pattern.

## 6. Closest Pair Analysis

Closest Pair identifies the two login locations with the minimum distance between them.

Before Optimisation:
- The algorithm compares each event with every other event.
- It includes self-comparisons and repeated pairs.
- It calculates unnecessary square roots.
- It incorrectly searches for the maximum distance.

After Optimisation:
- Self-comparisons are removed.
- Repeated pairs are avoided using j = i + 1.
- Squared distances are compared instead of actual distances.
- Square root is calculated only once at the end.

Time Complexity:
- Before: O(n²)
- After: O(n²)

The optimised version reduces unnecessary operations but does not change the overall time complexity.

## 7. Closest Pair – Distance Computation Comparison

Number of unique pairs = n(n-1)/2

| Input Size (n) | Before Optimisation (n²) | After Optimisation (Unique Pairs) |
|---|---:|---:|
| 1,000 | 1,000,000 | 499,500 |
| 4,000 | 16,000,000 | 7,998,000 |
| 8,000 | 64,000,000 | 31,996,000 |

Observation:

The optimised algorithm performs fewer distance calculations because it eliminates self-comparisons and repeated pairs. However, both algorithms have O(n²) time complexity.

## 8. Insertion Sort – Performance Comparison

| Input Size | Nearly Sorted (Already Descending) | Random Input |
|---|---:|---:|
| 1,000 | 999 | Approximately 250,000 |
| 4,000 | 3,999 | Approximately 4,000,000 |
| 8,000 | 7,999 | Approximately 16,000,000 |

Observation:

Insertion Sort performs efficiently when the input is already sorted or nearly sorted. However, it requires more comparisons for random input.

## 9. Overall Performance Comparison

| Algorithm | Before Optimisation | After Optimisation | Improvement |
|---|---|---|---|
| Insertion Sort | O(n²) worst case | O(n²) worst case | Correct sorting and stability |
| Blocklist Search | O(n) | O(1) average | Faster repeated searching |
| String Matching | O(nm) | O(nm) | Correct boundary checking |
| Closest Pair | O(n²) | O(n²) | Fewer distance calculations |

## 10. Conclusion

The analysis shows that optimisation improves the performance and correctness of the SentinelOps module.

- Insertion Sort correctly arranges alerts by severity.
- Set-based searching improves repeated blocklist lookups.
- String Matching correctly identifies all attack signatures.
- Closest Pair eliminates unnecessary distance calculations.

The experimental results support the theoretical analysis. Overall, the optimised algorithms reduce unnecessary operations and improve the efficiency and reliability of the SentinelOps SOC Alert-Triage Module.
