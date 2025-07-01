import collections
from typing import List


class Solution_DFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}

        visited = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
    

class Solution_Khans:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            indeg[c] += 1
            adj[p].append(c)

        q = collections.deque()
        for n in range(numCourses):
            if not indeg[n]:
                q.append(n)
        
        total = 0
        while q:
            cur = q.popleft()
            total += 1
            for n in adj[cur]:
                indeg[n] -= 1
                if not indeg[n]:
                    q.append(n)
        
        return total == numCourses