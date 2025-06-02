# 22. Generate Parenthesis
## Relevant Topics
String, Stack, Backtracking, Dynamic Programming

## Solution Thought Process
### Brute Force
```python
# perform a dfs/bfs to find all possible parenthesis of length 2n (n pairs)
# validate each combination at the end

# validation can be done by iterating through the string and keeping count of open parenthesis
# open - close should never be less than 0
```
Time Complexity: O((2^2n) * n) - 2^2n all possible combinations of length 2n, * n for linear validation.

### Backtracking
We are looking ALL possible parenthesis, so backtracking immediately comes to mind to explore all solutions. Furthermore, in observing the validation step, we see that the problem can be broken into smaller subproblems (finding subsequent parenthesis that satisfy the open-close condition)
```python
# initialize stack

# define backtrack(open, close)
#   if open == close == n (pairs satisfied)
#     append stack to results
#   if close <= open
#     append close
#     backtrack
#   if open < n
#     append open
#     backtrack
```