# 3202. Find the Maximum Length of Valid Subsequence II
## Relevant Topics
Parity

## Solution Thought Process
We see that from the problem statement, for any consecutive numbers a, b, c in the subsequence, (a+b)%k = (b+c)%k. We see that this implies that a%k = b%k. Therefore, there are two patterms:
1) All elements have the same remainder
2) Two remainders alternate
We use a 2D array to represent the maximum length of a valid subsequence whose last two elements have remainders (i + j) % k.