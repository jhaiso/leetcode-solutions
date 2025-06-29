# 286. Walls and Gates

## Relevant Topics

Array, Graphs, BFS

## Solution Thought Process
### Simultaneous BFS
Rather than searching from each piece of land, we begin multiple BFS's from each treasure chest. We simlutaneously search outwards, and the first BFS to reach any given node makes it the closest treasure chest.
