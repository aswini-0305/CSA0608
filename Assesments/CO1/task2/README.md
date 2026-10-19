TASK 2 – Identify the Basic Operation 
1. Linear Search
- Basic operation: Comparison between the target and each registration number (A[i] == key).
- Location: Inside the loop.
- Justification: Each comparison determines whether the target is found.
- Execution: Increases linearly with input size \(n\), up to \(n\) comparisons.
2. Recursive Binary Search
- Basic operation: Comparison of the target with the middle element (A[mid] == key).
- Location: At each recursive call.
- Justification: Each comparison helps eliminate half of the remaining search space.
- Execution: Increases logarithmically, requiring at most \(O(\log n)\) comparisons.
3. Hash-Based Search
- Basic operation: Hash-table lookup and key comparison when handling collisions.
- Location: During insertion and lookup in the hash table.
- Justification: Hashing directly identifies the likely location of the target.
- Execution: Expected \(O(1)\) lookup time, but may increase to \(O(n)\) in the worst case due to collisions.
