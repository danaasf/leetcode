# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.



# Definition for a Node.
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return 

        p = root 
        queue = deque([])
        queue.appendleft(p)

        while queue:
            size = len(queue)
            nxt = None
            for _ in range(size):

                node = queue.pop()
                if nxt:
                    node.next = nxt 
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
                
                nxt = node 
        
        return root


        