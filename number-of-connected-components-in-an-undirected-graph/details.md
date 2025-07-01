 # 323. Number of Connected Components in an Undirected Graph
 ## Relevant Topics
 Graph, BFS, DFS

 ## Solution Thought Process
 We run a traversal from each unvisited node. For each traversal, we increment the count of components by 1.

 Time Complexity: O(V+E)
 Space Complexity: O(V+E)