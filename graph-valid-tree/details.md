# 261. Graph Valid Tree

## Relevant Topics

Graph, Tree, BFS, DFS

## Solution Thought Process

We could do it with Khan's algorithm, but let's be interesting and do it with a DFS. We first make an adjacency map, and then we recursively run DFS on outneighbors. We keep track of the ones we've visited. We return false if there is a cycle, or if we visit less than 