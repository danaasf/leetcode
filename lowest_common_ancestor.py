# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val > q.val):
            temp =  q
            q=p
            p = temp 


        while (root):

            if(p.val<=root.val and q.val>=root.val):
                return root


            elif (p.val<root.val and q.val<root.val):
                root = root.left
                #both nodes are in left subTree
                #we want to reach a node that is larger than p and smaller than q 
        
                
            else:
                
                root= root.right
            #both nodes are in right subTree
        
        
    

sol = Solution()
root = [6,2,8,0,4,7,9,None,None,3,5] 
p = 2 
q = 8
print(sol.lowestCommonAncestor(root,p,q))