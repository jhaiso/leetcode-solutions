# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque([(root, 0)])
        while q:
            curr, depth = q.popleft()
            if depth < len(res):
                res[depth].append(curr.val)
            else:
                res.append([curr.val])
            if curr.left:
                q.append((curr.left, depth + 1))
            if curr.right:
                q.append((curr.right, depth + 1))

        return res