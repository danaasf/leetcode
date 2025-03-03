# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left 
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from cmath import inf
from typing import Optional

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validateSub(root: Optional[TreeNode],left,right):

            if (root ==None):
                return True 
            
            if (root.val <= left or root.val >= right):
                return False 

            return validateSub(root.left,left,root.val) and validateSub(root.right,root.val,right)

        
        return validateSub(root,-inf,inf)

            

        