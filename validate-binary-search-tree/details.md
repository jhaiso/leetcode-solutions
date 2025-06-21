# 98. Validate Binary Search Tree
## Relevant Topics
Tree, Binary Search Tree, BFS, DFS

## Solution Thought Process
The definition says the left and right subrees must also be binary search trees, so let's think recurisvely. We should keep track of the maximum and minimum found along the path to each node, since each node in the right subtree must be greater than the minimum and less than the maximum