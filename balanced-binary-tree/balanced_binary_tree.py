# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return (True, 0)
            l = dfs(curr.left)
            r = dfs(curr.right)
            if l[0] and r[0] and abs(l[1] - r[1]) < 2:
                return (True, 1 + max(l[1], r[1]))
            else:
                return (False, 0)
        
        return dfs(root)[0]