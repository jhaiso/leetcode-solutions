# 124. Binary Tree Maximum Path Sum
## Relevant Topics
Tree, Binary Tree, DFS, BFS

## Solution Thought Process
Whenever we think about trees, it's always a good idea to think recursively!

We need to keep track of the maximum, and find the maximal paths including both the left and right node.

Base case(s):
If the current node is null, we return 0 (sum of 0)

Recursive case(s):
We update the result using the maximal path including the current node
We return the current node and the maximal path to either the left or right