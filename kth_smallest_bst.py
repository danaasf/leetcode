# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from heapq import heappop, heappush, heapify, heappushpop
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []
        heapify(h)
        #pushing only while doing an inorder traversal, so this assures we're left with the k smallest 
        def traversal(node):
            if node is None:
                return

            if len(h) < k:
                heappush(h, -node.val)
            else:
                # If the current value is smaller than the largest in the heap, replace it
                if -node.val > h[0]:
                    heappushpop(h, -node.val)

            traversal(node.left)
            traversal(node.right)

        traversal(root)
        print(h)

        return -h[0]

               
            

        
        

