# Given the head of a linked list, rotate the list to the right by k places.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head 
        if not head:
            return head 
     
        size = 0
        while start:
            size += 1
            start = start.next 

        if k == 0 or k % size == 0:
            return head
        
        k = k%size 
        first = head 
        beginning1 = first
        
        i = 0
        while first and i< size-k-1 :
            i+=1
            first= first.next 
        
        second = first.next
        first.next = None

        beginning2 = second

        while second and second.next:
            second = second.next

        second.next = beginning1
        
        head = beginning2
        return head
    
        
