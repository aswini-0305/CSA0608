# Task 10 – Compare Theory with Experimental Behaviour

## 1. Theoretical and Experimental Comparison

The theoretical complexity of Linear Search is **O(n)**, Binary Search is **O(log n)**, and Dictionary Search is **O(1)** on average. These complexities are compared with the experimental execution times obtained for different input sizes.

- **Linear Search:** The execution time increases as the dataset size grows because elements may need to be checked one by one. This behaviour agrees with its theoretical time complexity of O(n).
- **Binary Search:** The execution time grows more slowly because the search space is halved at each step. Its observed behaviour generally agrees with the theoretical complexity of O(log n), provided the input is sorted.
- **Dictionary Search:** Lookup is generally very fast and has an average time complexity of O(1). However, its performance can vary due to hashing and collisions.

## 2. Scalability

As the input size increases from 1,000 to 1,000,000 registration numbers, Binary Search and Dictionary Search are generally expected to scale better than Linear Search. Dictionary Search offers fast average lookup, while Binary Search provides predictable logarithmic search performance on sorted data.

## 3. Differences Between Theory and Experiment

The measured execution times may not exactly match theoretical predictions. For small datasets, the differences between algorithms may be minimal because execution overhead can dominate the search time. For larger datasets, differences in growth rates are usually easier to observe.

## 4. Possible Reasons for Differences

- CPU speed and available memory.
- Operating system background processes.
- Python interpreter and function-call overhead.
- Dataset size and target position.
- Sorting and dictionary construction costs.
- Hash collisions and variations in memory access.
- Measurement noise during repeated executions.

## Conclusion

The theoretical and experimental analyses generally show that Linear Search becomes less efficient as the input size increases, whereas Binary Search and Dictionary Search provide better average scalability. However, Binary Search requires sorted data, and Dictionary Search requires preprocessing to construct the dictionary. Therefore, the most suitable algorithm depends on the dataset, preprocessing cost, and frequency of searches. The final comparison should be confirmed using the actual benchmark results and graphs.
