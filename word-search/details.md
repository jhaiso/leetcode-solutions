# 79. Word Search
## Relevant Topics
Backtracking

## Solution Thought Process
Because we need to explore all the potential adjacent cells, backtracking comes to mind. Since the condition exists that we can't use the same cell twice, we must use something to keep track of the existing path in the current traversal.