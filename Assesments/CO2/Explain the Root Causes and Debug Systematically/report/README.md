# B. EXPLAIN THE ROOT CAUSES AND DEBUG SYSTEMATICALLY

## 1. INTRODUCTION

The IP Blocklist Checking function is used in the SentinelOps Security Operations Centre (SOC) Alert-Triage Module. Its purpose is to identify whether a given IP address is present in the blocklist. Sequential search is used to compare the given IP address with each address in the list.

## 2. OBJECTIVE

1. To identify blocked IP addresses.
2. To detect errors in the original source code.
3. To correct the errors using systematic debugging.
4. To verify the corrected function using different test cases.

## 3. ORIGINAL FAULTY SOURCE CODE

    def is_blocked(blocklist, ip):
        for i in range(len(blocklist)):
            if blocklist[i] == ip:
                return False
            else:
                return False

## 4. IDENTIFICATION OF ERRORS

**Error 1 – Incorrect Return Statement**

The function returns False when an IP address matches. It should return True because the matching IP address is blocked.

**Error 2 – Premature Termination**

The else statement returns False immediately when the first IP address does not match. Therefore, the remaining IP addresses are not checked.

## 5. CORRECTED SOURCE CODE

    def is_blocked(blocklist, ip):
        for i in range(len(blocklist)):
            if blocklist[i] == ip:
                return True

        return False


    # Test data
    blocklist = [
        "10.0.0.5",
        "10.0.0.9",
        "172.16.4.2"
    ]

    queries = [
        "10.0.0.9",
        "10.0.0.5",
        "8.8.8.8"
    ]

    # Display results
    for ip in queries:
        result = is_blocked(blocklist, ip)
        print(ip, ":", result)

## 6. STEP-BY-STEP EXECUTION TRACE

Given blocklist:

10.0.0.5  
10.0.0.9  
172.16.4.2

**Query 1: 10.0.0.9**

Step 1: Compare 10.0.0.5 with 10.0.0.9 – Not matched.  
Step 2: Compare 10.0.0.9 with 10.0.0.9 – Matched.

Output: True

**Query 2: 10.0.0.5**

Step 1: Compare 10.0.0.5 with 10.0.0.5 – Matched.

Output: True

**Query 3: 8.8.8.8**

Step 1: Compare 10.0.0.5 with 8.8.8.8 – Not matched.  
Step 2: Compare 10.0.0.9 with 8.8.8.8 – Not matched.  
Step 3: Compare 172.16.4.2 with 8.8.8.8 – Not matched.

Output: False

## 7. TESTING AND VERIFICATION

Test Case 1: Input – 10.0.0.9; Expected Output – True; Actual Output – True.

Test Case 2: Input – 10.0.0.5; Expected Output – True; Actual Output – True.

Test Case 3: Input – 8.8.8.8; Expected Output – False; Actual Output – False.

Test Case 4: Empty blocklist []; Expected Output – False; Actual Output – False.

Test Case 5: Input – 172.16.4.2; Expected Output – True; Actual Output – True.

All test cases produce the expected results.

## 8. COMPLEXITY ANALYSIS

Best Case: O(1) – IP address found at the first position.

Average Case: O(n) – Multiple addresses are checked.

Worst Case: O(n) – IP address found at the last position or not found.

Space Complexity: O(1), because sequential search uses constant extra memory.

## 9. RESULT

The IP Blocklist Checking function was successfully debugged using sequential search. The incorrect return value and premature termination errors were corrected. The corrected program successfully identifies blocked and unblocked IP addresses and passes the boundary test cases.

## 10. CONCLUSION

Systematic debugging helped identify and correct the logical errors in the original program. The corrected function checks every address in the blocklist until a match is found. It produces accurate results and is suitable for the basic IP blocklist checking operation in the SentinelOps SOC Alert-Triage Module.
