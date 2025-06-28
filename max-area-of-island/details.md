# 695. Max Area of Island

## Relevant Topics

Array, Graph, BFS, DFS

## Solution Thought Process

We have to find the maximal connected component. Therefore, we keep track of the nodes that we've included in another 'island', and we run a DFS/BFS if we encounter one not yet included.

Optimization trick: grid can also be used to keep track of the visited nodes (they can be converted to water lol)

Time Complexity: O(n*m)
Space Complexity: O(n*m)