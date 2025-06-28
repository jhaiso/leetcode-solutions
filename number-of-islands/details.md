# 200. Number of Islands

## Relevant Topics

Arrays, Graph, BFS, DFS

## Solution Thought Process

Each island is a group of connected pieces of land. We begin a traversal if we see a node that has not yet been traversed.

```python
# initialize 2D array to keep track of visited
# for each row
#   for each column
#       if the current node isn't visited
#           run a bfs
#           increment the number of islands by 1
```
Time Complexity: O(n*m)
Space Complexity: O(n*m)