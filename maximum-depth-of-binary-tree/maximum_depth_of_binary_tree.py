# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        stack = [(root, 0)]
        while stack:
            curr, depth = stack.pop()
            if not curr:
                res = max(res, depth)
                continue
            stack.append((curr.left, depth + 1))
            stack.append((curr.right, depth + 1))

        return res