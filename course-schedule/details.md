# 207. Course Schedule

## Relevant Topics

Graph, DFS, Topological Sort

## Solution Thought Process
Because we're dealing with courses and prerequisites, we must ensure that the graph is a DAG.

### DFS
We can run a DFS from each class, and if we revisit a node that has already been visited in the DFS, then we return false.

Time Complexity: O(V+E)
Space Complexity: O(V+E)

### Khan's Algorithm