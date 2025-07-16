# 3201. Find the Maximum Length of Valid Subsequence I
## Relevant Topics
Array, Enumeration

## Solution Thought Process
We see that based on the conditions, we are looking for the longest subsequence of elements such that the difference between each adjacent one is either strictly ODD or EVEN. Therefore, we see that we can count the evens, odds, and elements where the previous element is a different parity than the current one.

Time Complexity: O(n)
Space Complexity: O(1)