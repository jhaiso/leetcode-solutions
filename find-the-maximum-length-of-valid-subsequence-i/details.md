# 3201. Find the Maximum Length of Valid Subsequence I
## Relevant Topics
Array, Enumeration

## Solution Thought Process
We see that based on the conditions, we are looking for the longest subsequence of elements such that the difference between each adjacent one is either strictly ODD or EVEN. Therefore, by definition, all elements at even indices have the same parity, and all elements at odd indices have the same parity. We can enumerate these possibilities.

Time Complexity: O(n)
Space Complexity: O(1)