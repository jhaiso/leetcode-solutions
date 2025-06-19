# 110. Balanced Binary Tree

## Relevant Topics

Tree, Binary Tree, DFS, BFS

## Solution Thought Process

By definition: "A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one."

Therefore we need to keep track of two things: 1. if the subtree is valid, 2. the maximum depth of the subree

```python
# define function dfs(curr)
#   if curr is null
#       return (True, 0)    # by definition it is balanced, and the depth is 0
#   l = dfs(curr.left)
#   r = dfs(curr.right)
#   if abs(l[1] - r[1]) < 2 and both subtrees balanced
#       return (True, max(l[1], r[1]))
```