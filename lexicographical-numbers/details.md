# 386 Lexicographical Numbers

## Relevant Topics

Array, Math, DFS

## Solution Thought Process
### Brute Force
Convert all the numbers into strings, sort, return.
Time Complexity: O(n*m + nlogn), m is number of digits of largest number
Space Complexity: O(n*m)

### DFS
Intuitively, when writing the numbers in lexicographical order, we multiply by 10 until we reach maximal depth (1, 10, 100, etc). Then, we append the digits 1-9 to the end (1, 10, 100, 101, 102, etc). We see that we can do a depth first search here.
Time Complexity: O(n)
Space Complexity: O(logn), (log base 10 for each of the 10 digits)

### Iteration
When writing down the numbers by hand, we have the following intution. If the number * 10 is less than n, then we write it down. Otherwise, we write the digits 1-9. If the previous last digit was a 9 or is not <= n>, then we perform integer division by 10, and add 1 until the number no longer ends in 9.
ex. n = 23 --> 1, 10, 11, ..., 19 -->(integer division by 10) 1 -->+1 2 , 20, etc