import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            indeg[crs] += 1
            adj[pre].append(crs)
        
        q = collections.deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for crs in adj[cur]:
                indeg[crs] -= 1
                if indeg[crs] == 0:
                    q.append(crs)
        
        return res if len(res) == numCourses else []
