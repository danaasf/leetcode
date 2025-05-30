# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def traverse(node_l,node_r):
            if ((not node_l) and node_r) or (node_l and (not node_r)):
                return False
            elif (not node_l and not node_r):
                return True
            else:
                if node_l.val != node_r.val:
                    return False
                return traverse(node_r.left,node_l.right) and traverse(node_l.left, node_r.right)
                
        
        return traverse(root.left,root.right)


            
            
            
        