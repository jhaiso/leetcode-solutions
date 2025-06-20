# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        leftLca = self.lowestCommonAncestor(root.left, p, q)
        rightLca = self.lowestCommonAncestor(root.right, p, q)

        if leftLca and rightLca:
            return root
        
        return leftLca if leftLca else rightLca