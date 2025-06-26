# 2311. Longest Binary Subsequence Less Than or Equal to K
## Relevant Topics
String, Greedy

## Solution Thought Process
### Greedy
We see that it is always possible to include all the zeros. Each additional zero doubles the value of each 1, and will remove <= 1 valid 1. Therefore, we include all the zeros, then as many ones as possible!