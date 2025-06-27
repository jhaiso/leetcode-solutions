# 90. Subsets II

## Relevant Topics

Array, Backtracking

## Solution Thought Process

Because we are looking for ALL possible subsets, backtracking comes to mind. Additionally, since we are avoiding duplicates, sorting comes to mind.

```python
# define result array
# define current
# function backtrack(idx)
#   if idx is the length of nums
#       add to result
#       return
#   otherwise
#   for each index from idx to the length of nums
#       if index > idx and nums[index] = nums[index-1]
#           continue
#       otherwise
#       append element to current
#       backtrack
#       remove
```
Time Complexity: O(n * 2^n)
Space Complexity: O(2^n)