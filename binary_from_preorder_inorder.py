# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
                return None

        root = TreeNode(preorder[0], None, None)
        root_inorder = 0

        
        root_inorder = inorder.index(root.val) 

       
        size_left = root_inorder 
        size_right= len(inorder) - root_inorder - 1
        
        new_pre_left = preorder[1:1 + size_left]
        new_pre_right = preorder[1 + size_left:]


        root.left = self.buildTree(new_pre_left,inorder[0:root_inorder])
        root.right = self.buildTree(new_pre_right,inorder[root_inorder+1: len(inorder)])

        return root
        