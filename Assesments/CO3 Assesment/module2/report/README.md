# MODULE 2 – LIVE SELLER LEADERBOARD

## 1. AIM

To sort seller scores efficiently using the Quick Sort algorithm. The system must update the leaderboard quickly whenever seller scores change.

## 2. PROBLEM DESCRIPTION

In an online selling platform, seller scores are updated frequently based on sales and performance.

The leaderboard must arrange seller scores in ascending order. Since only a few scores change between refreshes, the data is usually nearly sorted.

The existing implementation uses Quick Sort with the first element as the pivot. This can cause poor performance when the input is already sorted or nearly sorted.

Therefore, an improved pivot selection strategy is required.

## 3. ALGORITHM USED

**Quick Sort with Median-of-Three Pivot Selection**

Quick Sort is a divide-and-conquer sorting algorithm. It selects a pivot element and partitions the array into two parts.

Median-of-Three selects the median value among the first, middle and last elements as the pivot.

This helps reduce the possibility of highly unbalanced partitions.

## 4. WORKING PRINCIPLE

Quick Sort works using three main steps:

**1. Pivot Selection:**
- Select a pivot element.
- Use Median-of-Three to select a suitable pivot from the first, middle and last elements.

**2. Partitioning:**
- Place smaller elements before the pivot.
- Place larger elements after the pivot.
- Place the pivot in its correct sorted position.

**3. Recursion:**
- Apply Quick Sort to the left and right partitions.
- Continue until the complete list is sorted.

## 5. SAMPLE INPUT

Given seller scores:

42, 17, 63, 8, 55, 29

## 6. STEP-BY-STEP EXECUTION

**Step 1: Select the pivot**

First element = 42

Middle element = 63

Last element = 29

Using Median-of-Three:

Median of (42, 63, 29) = 42

Therefore, pivot = 42.

**Step 2: Partitioning**

Original list:

[42, 17, 63, 8, 55, 29]

Compare each element with pivot 42.

- 17 is smaller than 42.
- 63 is greater than 42.
- 8 is smaller than 42.
- 55 is greater than 42.
- 29 is smaller than 42.

After partitioning:

[17, 8, 29, 42, 55, 63]

The pivot 42 is now in its correct position.

**Step 3: Sort the left partition**

Left partition:

[17, 8, 29]

After sorting:

[8, 17, 29]

**Step 4: Sort the right partition**

Right partition:

[55, 63]

After sorting:

[55, 63]

**Step 5: Final sorted list**

[8, 17, 29, 42, 55, 63]

## 7. SAMPLE OUTPUT

Original Scores:

[42, 17, 63, 8, 55, 29]

Sorted Scores:

[8, 17, 29, 42, 55, 63]

## 8. TIME COMPLEXITY

| Case | Time Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n²) |

**Explanation:**

- Best Case: The pivot divides the array into nearly equal parts.
- Average Case: The partitions are reasonably balanced.
- Worst Case: The pivot repeatedly produces highly unbalanced partitions.

## 9. RECURRENCE RELATION

**Best Case:**

T(n) = 2T(n/2) + O(n)

Using the Master Theorem:

T(n) = O(n log n)

**Worst Case:**

T(n) = T(n-1) + O(n)

Expanding:

T(n) = T(n-2) + O(n-1) + O(n)

T(n) = O(1 + 2 + 3 + ... + n)

Therefore:

T(n) = O(n²)

## 10. IMPROVED PIVOT STRATEGY

The existing implementation selects the first element as the pivot.

This may produce unbalanced partitions when the data is already sorted or nearly sorted.

To improve performance, Median-of-Three Pivot Selection is used.

It selects the median of:
- First element
- Middle element
- Last element

This strategy reduces the likelihood of unbalanced partitions and improves practical performance.

However, it does not guarantee O(n log n) worst-case performance.

## 11. SPACE COMPLEXITY

- Average Case: O(log n)
- Worst Case: O(n)

Quick Sort requires memory for recursive function calls.

A carefully implemented iterative version or recursion-depth protection can reduce the risk of excessive stack usage.

## 12. ADVANTAGES

1. Efficient for average-case sorting.
2. Uses an in-place partitioning approach.
3. Requires relatively little additional memory.
4. Median-of-Three improves pivot selection.
5. Suitable for frequently updated leaderboard data.

## 13. DISADVANTAGES

1. Worst-case time complexity is O(n²).
2. Performance depends on pivot selection.
3. Recursive calls may increase memory usage.
4. It is not a stable sorting algorithm.

## 14. RESULT

Thus, the seller scores were successfully sorted in ascending order using Quick Sort with Median-of-Three Pivot Selection.

The improved pivot strategy reduces the possibility of unbalanced partitions compared with always selecting the first element.

Therefore, Quick Sort with an improved pivot strategy is a suitable choice for the Live Seller Leaderboard module.
