from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(v, p):
            if visited[v]:  # this is important to check because the graph may be cyclic
                return
            visited[v] = True
            for nei in adj[v]:
                if nei == p:
                    continue
                dfs(nei, v)
        
        visited = [False] * n
        res = 0
        for v in range(n):
            if visited[v]:
                continue
            res += 1
            dfs(v, -1)
        
        return res