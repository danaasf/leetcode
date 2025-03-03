# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 
class Solution:
    def traverse(self, root: Optional[TreeNode], diameter: [int]) : # type: ignore
        if (root is None):
            return 0            

        left = self.traverse(root.left,diameter)
        right = self.traverse(root.right,diameter)

        diameter[0] = max(diameter[0], left+right)

        return 1+ max(left,right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #we want to go from the very left to the very right
        #we use two counter 
        diameter = [0]
        self.traverse(root,diameter)
        return diameter[0]
        
            