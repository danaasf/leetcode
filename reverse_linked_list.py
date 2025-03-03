# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #each time I have to keep track of the previous node and the current node

        if head is None:
            return head 

        current_node = head
        prev_node = None 
        next_node = None 
        
        while (current_node):
            next_node = current_node.next 
            current_node.next=prev_node
            prev_node= current_node
            current_node= next_node 
            
        return prev_node





        
       
        