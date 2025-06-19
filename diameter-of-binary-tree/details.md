# 543. Diameter of Binary Tree

## Relevant Topics

Binary Tree, BFS, DFS

## Solution Thought Process

We see that the longest path passing through any node is the sum of the depth of the left subree and the depth of the right subtree.

```python
# define variable to keep track of longest

# function dfs(curr)
#   if current is null
#       return 0
#   set result to the maximum of itself and left + right
#   return 1 + maximum of left & right
```