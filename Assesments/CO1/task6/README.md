# Task 6 – Formulate the Recurrence Relation

## Problem

A recurrence relation expresses the running time of a recursive algorithm in terms of the running time of smaller subproblems. Among the proposed approaches, recursive Binary Search is suitable for formulating a recurrence relation because it repeatedly reduces the search space by half.

## Approach: Recursive Binary Search

**Input Size:** n, the number of sorted student registration numbers.

**Recursive Subproblem:** After comparing the target with the middle element, the algorithm continues searching in either the left half or the right half. The size of the next subproblem is approximately n/2.

**Number of Recursive Calls:** Only one recursive call is made at each step because the algorithm searches either the left half or the right half, not both.

**Work Performed Outside the Recursive Call:** The algorithm calculates the middle index and compares the target with the middle element. These operations require constant time, represented by c.

## Derivation of the Recurrence Relation

At the beginning, the algorithm receives n registration numbers.

Step 1: If the target is equal to the middle element, the algorithm returns the position immediately.

Step 2: If the target is smaller than the middle element, the algorithm recursively searches the left half.

Step 3: If the target is greater than the middle element, the algorithm recursively searches the right half.

Step 4: In either case, the size of the recursive subproblem becomes approximately n/2.

Step 5: Apart from the recursive call, the algorithm performs a constant amount of work to calculate the middle index and compare values.

Therefore, the running time for an input of size n consists of the time required for one subproblem of size n/2 and the constant work performed at the current step.

Hence, the recurrence relation is:

T(n) = T(n/2) + c, for n > 1

where:
- T(n) represents the running time for n registration numbers.
- T(n/2) represents the running time for the recursive subproblem.
- c represents the constant work performed at each recursive step.

## Base Case

The recursion stops when the search space contains one element or becomes empty.

For a single element:

T(1) = c₀

where c₀ is a constant representing the time required to check the element and return the result.

If the target is not found, the algorithm also terminates when the search interval becomes empty, requiring constant additional work.

## Final Recurrence Relation

T(n) = T(n/2) + c, for n > 1

T(1) = c₀

## Conclusion

The recurrence relation is derived directly from the behaviour of recursive Binary Search. Each recursive call reduces the problem size by half, makes only one recursive call, and performs constant work outside that call. Solving this recurrence gives a logarithmic running time of Θ(log n), making recursive Binary Search efficient for searching large, sorted student registration-number datasets.
