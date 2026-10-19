# Task 9 – Experimental Performance

## How to Run

Execute `python Task_8_Implementation_Testing/Source_Code/search_experiments.py` from the repository root. The program generates `performance_results.csv`, `execution_time.png`, `comparison_count.png`, and `preprocessing_time.png` in `Report/Tables_and_Graphs/`.

## Method

- Dataset sizes: 1,000; 10,000; 100,000; and 1,000,000.
- Registration numbers are unique integers.
- Test cases include first, middle, last, and absent targets.
- Search execution time is measured using `time.perf_counter()` and the median of five repetitions.
- Preprocessing time is measured separately.
- Correctness is verified for every algorithm and test case.
- Linear and binary search record explicit key comparisons. Python dictionary lookup comparison counts are left blank because internal probes and equality comparisons are not directly exposed.

## Results

After running the benchmark, insert the measured results into the summary tables and discuss the generated graphs. Do not use invented execution times.

| Input Size | Linear Search | Binary Search | Dictionary Search |
|---:|---:|---:|---:|
| 1,000 | Actual result | Actual result | Actual result |
| 10,000 | Actual result | Actual result | Actual result |
| 100,000 | Actual result | Actual result | Actual result |
| 1,000,000 | Actual result | Actual result | Actual result |

Record execution times in milliseconds and use the generated `performance_results.csv` for the actual measurements.

## Graphs

- **Execution Time:** `execution_time.png` compares the search execution times.
- **Comparison Count:** `comparison_count.png` compares key comparisons for linear and binary search.
- **Preprocessing Time:** `preprocessing_time.png` compares sorting and dictionary construction costs.

## Interpretation

1. Linear search generally takes longer as the input size increases.
2. Binary search grows more slowly because it repeatedly halves the search space.
3. Dictionary lookup is generally close to constant time on average.
4. Sorting and dictionary construction require preprocessing time.
5. Execution-time variations may result from system load, hardware, memory usage, or Python version.

## Environment Details

- Python version: Record the installed version.
- Operating system: Record the operating system used.
- CPU and RAM: Record the available hardware specifications.
- Benchmark modifications: Record any changes made to the original implementation.

## Conclusion

The experiment evaluates Linear Search, Binary Search, and Dictionary Search using different input sizes. Execution time, key comparisons, and preprocessing costs are used to compare their performance. The measured results and graphs help identify the most suitable search algorithm for different dataset sizes.
