# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        path1 = []
        path2 = []

        def dfs(root,path,target):
            if root is None:
                return False
            path.append(root)
            if root == target:
                return True
            if dfs(root.left,path,target) or dfs(root.right,path,target):
                return True
        
            path.pop()
            return False

        dfs(root,path1,p)
        dfs(root,path2,q)

        # my thought process is we do a dfs on root to find p and q and we save the path for each node in an array
        # we return the last node that is mutual for each array/path
        i = 1
        # we know at least the global root is common that's why we intialize the i to 1 

        while i<len(path1) and i<len(path2):
            if path1[i]!=path2[i]:
                return path1[i-1]
            i+=1

        return path1[i-1]
