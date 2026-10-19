# TASK 1 – Design the Algorithm

## Problem

Given unique student registration numbers and a target registration number, determine whether the target exists and return its position or record.

## Approach 1: Iterative Linear Search

**Strategy:** Sequential search. It checks records from the beginning until a match is found or the list ends. No preprocessing is required.

### Pseudocode

```text
LINEAR_SEARCH(A, key)
    for i = 0 to length(A)-1
        if A[i] == key
            return i
    return -1
```

**Why investigate it?** It is simple, works on unsorted data, and provides a baseline. However, it becomes expensive for large datasets and repeated searches.

**Time Complexity:** O(n)

## Approach 2: Recursive Binary Search

**Strategy:** Divide and Conquer. It compares the target with the middle element and recursively searches the appropriate half.

**Preprocessing:** The registration numbers must be sorted in ascending order.

### Pseudocode

```text
BINARY_SEARCH(A, low, high, key)
    if low > high
        return -1

    mid = (low + high) // 2

    if A[mid] == key
        return mid
    else if key < A[mid]
        return BINARY_SEARCH(A, low, mid-1, key)
    else
        return BINARY_SEARCH(A, mid+1, high, key)
```

**Why investigate it?** It reduces the search space by half at each step and is efficient for large, sorted datasets.

**Time Complexity:** O(log n)

## Approach 3: Hash-Based Search

**Strategy:** Hashing. A hash function maps registration numbers to locations in a hash table for fast lookup.

**Preprocessing:** Create a hash table and insert the registration numbers.

### Pseudocode

```text
HASH_SEARCH(H, key)
    if key exists in H
        return H[key]
    else
        return -1
```

**Why investigate it?** Hashing provides fast average lookup and is useful for repeated searches. It requires additional memory to store the hash table.

**Expected Search Time:** O(1)

## Comparison of Approaches

| Feature | Linear Search | Binary Search | Hash-Based Search |
|---|---|---|---|
| Strategy | Brute Force | Divide and Conquer | Hashing |
| Implementation | Iterative | Recursive | Hash Table |
| Sorting Required | No | Yes | No |
| Expected Search Time | O(n) | O(log n) | O(1) |
| Extra Space | O(1) | O(log n) recursion stack | O(n) |

## Conclusion

Linear search is suitable for small or unsorted datasets. Binary search performs efficiently on sorted data, while hashing provides fast average lookup for repeated searches. Comparing these approaches helps identify the most suitable algorithm for student registration-number searching.
