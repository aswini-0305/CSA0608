# Task 7 – Solve the Recurrence Relation

## Problem

The recurrence relation obtained in Task 6 for Recursive Binary Search is:

T(n) = T(n/2) + c, for n > 1

T(1) = c₀

where T(n) represents the running time for n student registration numbers, T(n/2) represents the time required for the recursive subproblem, c is the constant work performed at each step, and c₀ is the base-case cost.

## Method Selected: Iteration Method

The iteration method is appropriate because Binary Search reduces the input size by half at every recursive call and performs constant work outside the recursive call. By repeatedly expanding the recurrence, we can determine the total number of steps required.

## Step 1: Expand the Recurrence

Given:

T(n) = T(n/2) + c

Substituting T(n/2):

T(n) = [T(n/4) + c] + c

T(n) = T(n/4) + 2c

Substituting T(n/4):

T(n) = [T(n/8) + c] + 2c

T(n) = T(n/8) + 3c

Continuing this process:

T(n) = T(n/2ᵏ) + kc

## Step 2: Determine the Number of Recursive Steps

The recursion stops when the subproblem size becomes 1.

Therefore:

n / 2ᵏ = 1

n = 2ᵏ

Taking logarithms to base 2:

k = log₂ n

Thus, the number of recursive steps is proportional to log₂ n.

## Step 3: Substitute the Number of Steps

From the expanded recurrence:

T(n) = T(n/2ᵏ) + kc

Substituting k = log₂ n and n/2ᵏ = 1:

T(n) = T(1) + c log₂ n

Since T(1) = c₀:

T(n) = c₀ + c log₂ n

Here, c₀ and c are constants.

## Step 4: Determine the Time Complexity

The term c₀ is constant, while c log₂ n grows logarithmically as n increases.

Ignoring constant factors and lower-order terms:

T(n) = Θ(log n)

Therefore, the time complexity of Recursive Binary Search is Θ(log n).

## Interpretation

The result indicates that Recursive Binary Search is efficient for large, sorted student registration-number datasets because each recursive call eliminates approximately half of the remaining elements.

For example:

- For 1,000 records, approximately 10 comparisons may be sufficient.
- For 1,000,000 records, approximately 20 comparisons may be sufficient.

Thus, increasing the dataset size by a factor of 1,000 requires only about 10 additional comparisons in the worst case.

## Conclusion

The recurrence relation T(n) = T(n/2) + c was solved using the iteration method. The derivation shows that the number of recursive steps is proportional to log₂ n. Therefore, the running time of Recursive Binary Search is Θ(log n), making it suitable for searching large, sorted student registration-number datasets.
