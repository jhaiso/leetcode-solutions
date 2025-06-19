# 104. Maximum Depth of Binary Tree

## Relevant Topics

Binary Tree, Recursion, DFS, BFS

## Solution Thought Process

Whenever we think about trees, it's always a good idea to think recursively...
Base Case:
when the current node is null, we return 0 as the depth

Recursive Case:
otherwise, we add one to the maximum of the depth of the left and right subtrees
