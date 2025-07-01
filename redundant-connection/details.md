# 684. Redundant Connection

## Relevant Topics

Graph, DFS, Khan's Algorithm, Disjoint Set Union

## Solution Thought Process
We can utilize a union find to find the edge that connects two nodes with the same parent.

Time Complexity: O(V+(E*alpha(V))) - alpha is amortized complexity
Space Complexity: O(V)