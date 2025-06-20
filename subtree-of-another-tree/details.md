# 572. Subtree of Another Tree
## Relevant Topics
Tree, Binary Tree, DFS, BFS, String Matching

## Solution Thought Process
### DFS
We could perform a DFS/BFS through the tree, and when the current node matches the root node of the subtree, we compare the two subtrees.
Time Complexity: O(n*m)
Space Complexity: O(n+m)

### String Matching
We could serialize the tree and subtree. Then, using string matching, we can find if the subtree exists in the tree. Python's built in 'in' operator utilizes Boyer Moore (O(n*m)). While the average performance is typically better because of the skipping behavior, we can improve the worst-case time complexity by using the z-algorithm.
Time Complexity: O(n+m)
Space Complexity: O(n+m)
