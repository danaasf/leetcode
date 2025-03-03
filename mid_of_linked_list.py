# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#         Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        length = 1
        middle = 0 
        while (pointer):
            pointer = pointer.next 
            length += 1

        
        middle= ( length-1 ) // 2
        
        print (middle)
        for i in range(0,middle):
            head = head.next 
        
        return head

        
