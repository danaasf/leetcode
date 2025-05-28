# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# You are given the beginning of a linked list head, and an integer n.

# Remove the nth node from the end of the list and return the beginning of the list.

# Example 1:

# Input: head = [1,2,3,4], n = 2

# Output: [1,2,4]
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: 
            return head

        size = 0
        pointer = head
        while pointer:
            size+=1
            pointer = pointer.next
        
        target = size - n
        ind = head
        prev = head
        
        if target == 0 :
            return head.next 

        while target > 0:
            prev = ind 
            ind = ind.next
            target -=1
        temp = ind.next
        prev.next = temp

        return head


        