# 100. Same Tree

## Relevant Topics

Tree, Binary Tree, BFS, DFS

## Solution Thought Process

By definition: "Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

It's a tree problem, so let's think recursively!

Base Case(s):
If neither node exists, we return True
If only one node exists, we return False

Recursive Case:
If both nodes exist and their values are the same, we return left and right

```python
# def sameTree(p, q)
#   
```