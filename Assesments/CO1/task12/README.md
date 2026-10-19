# TASK 12 – Re-evaluate and Adapt the Design

## A. Impact Analysis 

The university's requirements have changed. The system must now handle **50,000 search requests per hour** using a database containing **1,000,000 student records**. New student records are added only once per day.

- **Changed requirements:** The database is large, and the system must support frequent searches with minimal response time.
- **Affected assumptions:** The original design must now consider high search frequency, scalability, memory usage, and the cost of updating records.
- **Importance of search frequency:** With 50,000 searches per hour, the system processes approximately 13.9 searches per second on average. Efficient retrieval is important to maintain responsiveness.
- **Low update frequency:** Since new records are added only once per day, the system can build or refresh its search index periodically without repeatedly paying the preprocessing cost.

Therefore, the revised design should prioritize fast searches while keeping daily updates efficient.

## B. Evaluation of the Original Design 

The original design recommended Dictionary Search using a Python dictionary.

- **Expected behaviour:** Dictionary lookup has an average time complexity of O(1), making it suitable for frequent searches across one million records.
- **Preprocessing cost:** Building the dictionary generally takes O(n) time on average. Since records are added only once per day, this cost is acceptable for many applications.
- **Alternative approach:** Binary Search provides O(log n) lookup on sorted records, but maintaining the sorted order requires additional processing. A database index on the registration number is another practical option.

The original dictionary-based design remains suitable for fast in-memory searches. However, a persistent database index may be preferable when durability, concurrent access, and reliable daily updates are required.

## C. Adaptation or Redesign 

**Decision: MODIFY the original design.**

The revised strategy will use a database table with a unique index on the student registration number. If an in-memory Python application is required, a dictionary can also be maintained as a lookup structure.

The revised design follows these steps:

1. Store student records in a persistent database.
2. Create a unique index on the registration-number field.
3. Process search requests through indexed lookups.
4. Insert new student records daily and update the index automatically.
5. Run performance tests under realistic concurrent search loads.

**Computational complexity:**

- Dictionary lookup: O(1) average.
- Dictionary construction: O(n) average.
- Binary Search: O(log n) per search on sorted data.
- Balanced database index lookup: typically O(log n), depending on the index structure.
- Indexed insertion: typically O(log n), depending on the database index.

This modification preserves fast retrieval while improving persistence, update management, and support for multiple users.

## D. Evidence-Based Defence 

The modified design is justified by the database size, search frequency, and low update rate.

- **Mathematical analysis:** Dictionary Search offers O(1) average lookup, while indexed database searches are typically O(log n).
- **Search frequency:** The system must handle 50,000 requests per hour, or approximately 13.9 requests per second on average. Peak traffic may be higher.
- **Preprocessing:** Daily record additions allow the system to update its index incrementally rather than rebuilding the entire search structure after every insertion.
- **Dataset size:** One million records makes sequential Linear Search, with O(n) time per request, less attractive for frequent retrieval.
- **Computational trade-offs:** Dictionary Search consumes additional memory, whereas database indexing introduces storage and maintenance overhead but provides persistence and concurrency support.
- **Experimental evidence:** The actual execution-time and comparison-count results from Task 9 should be used to verify the performance differences. No unmeasured timing values should be assumed.

## Conclusion

The original Dictionary Search approach remains efficient for frequent student-record retrieval, but the changed operating conditions justify modifying the overall system to use a persistent database with a unique index on registration numbers. This design supports one million records, frequent searches, and daily additions while balancing lookup speed, preprocessing cost, memory usage, and data reliability. Final performance should be validated using the benchmark results and a realistic concurrent-load test.
