# 133. Clone Graph

## Relevant Topics

Graph, Hash Map, BFS

## Solution Thought Process
The issue with making a deep copy is that there's a possibility that we create an edge from an existing node to one that doesn't exist, so we need to ensure that each new node is created before making the edge between them. But, we need to make multiple edges to the same new node, so we keep a map that takes the old node as the key, and stores the new node as the value!