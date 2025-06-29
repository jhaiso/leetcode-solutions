# 994. Rotting Oranges

## Relevant Topics

Array, Graph, BFS

## Solution Thought Process

We have to find the distance of the closest rotting orange to each fresh orange. Then we have to compare the number of discovered oranges to the total number of oranges.

```python
# loop through grid and count oranges and locate rotten oranges
# simultaneous BFS
# return the largest distance if all oranges discovered, otherwise -1
```