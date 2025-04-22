# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from leetcode.linked_list_cycle import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        half = 0 
        p = head 

        while (p):
            stack.append(p)
            p = p.next 

        end = stack.pop()
        start = head 

        while stack and end != start and start.next != end:
            next_node = start.next

            start.next = end
            end.next = next_node

            start = next_node
            end = stack.pop()
        end.next = None
        

            


        
            


        



            
        