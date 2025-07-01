# 130. Surrounded Regions

## Relevant Topics

Array, Graph, DFS, BFS

## Solution Thought Process

### DFS

We can run a traversal from each "O" that lies on the outer edge of the grid. If we discover an "O", then that "O" will become an "X".

```python
# Initialize visited array
# Run a DFS from each outer "O"
# Traverse through the grid without the edges
#   if a value is visited
#       change it to "X"
```
