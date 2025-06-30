# 417. Pacific Atlantic Water Flow

## Relevant Topics

Array, Graph, DFS, BFS

## Solution Thought Process
### Brute Force
The brute force solution would be to run a traversal from each cell.

### DFS/BFS
Rather than starting at the cells, we start at the oceans. We run a BFS/DFS from each cell adjacent to the oceans, and add the discovered values to two sets. Then, the result is the union of the two sets. We make sure to keep a track of visited cells.

Time Complexity: O(m*n)
Space Complexity: O(m*n)