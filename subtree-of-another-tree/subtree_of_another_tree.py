# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution_DFS:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p, q):
        if not (p or q):
            return True
        if (p and q) and (p.val == q.val):
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        
class Solution_String:
    def serialize(self, root):
        if not root:
            return "$#"
        return "$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right)
    
    def z_function(self, s):
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1, n):
            if i <= r:
                z[i] = min(z[i - l], r - i + 1)
            while i + z[i] < n and s[z[i]] == s[z[i] + i]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
        return z


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized = self.serialize(root)
        serialized_sub = self.serialize(subRoot)
        concat = serialized_sub + "|" + serialized
        z = self.z_function(concat)

        sub_length = len(serialized_sub)
        for i in range(sub_length + 1, len(z)):
            if z[i] == sub_length:
                return True
        return False