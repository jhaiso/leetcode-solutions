# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        
        def inorder(curr):
            nonlocal count, k
            if not curr:
                return 0
            left = inorder(curr.left)
            count += 1
            if count == k:
                return curr.val
            right = inorder(curr.right)
            return left if left else right
        
        return inorder(root)