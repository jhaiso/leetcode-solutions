# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(curr, minimum, maximum):
            if not curr:
                return True
            if not (curr.val > minimum and curr.val < maximum):
                return False
            return validate(curr.left, minimum, curr.val) and validate(curr.right, curr.val, maximum)

        return validate(root, float('-inf'), float('inf'))