# 1448. Count Good Nodes in Binary Tree
## Relevant Topics
Tree, Binary Tree, DFS, BFS

## Solution Thought Process
We need to keep track of the maximum node in the path (since if there exists a node greater than the current node, the maximum is guaranteed to be one of those nodes).