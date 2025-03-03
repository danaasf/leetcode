# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque ([])
        res = []
        if root is None:
            return res

        queue.append(root)
        
        while queue: 
            lenq = len(queue)
            
            for i in range(lenq):
                node = queue.popleft()
                
                # The last node in the level is the rightmost one.
                if i == lenq - 1:
                    res.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
  
        return res
            



