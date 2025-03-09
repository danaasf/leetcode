# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:

# Input: lists = []
# Output: []
# Example 3:

# Input: lists = [[]]
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

from leetcode.linked_list_cycle import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        

        for i in range(0,len(lists)):
            if not lists[i]:
                continue
            p = lists[i]
            val = p.val
            heapq.heappush(heap,(val,i,p))

        new_list = ListNode() 
        curr = new_list
        while heap:
            popped = heapq.heappop(heap)
            curr.next= popped[2]
            if (popped[2].next):
                heapq.heappush(heap,(popped[2].next.val,popped[1],popped[2].next))
            curr= curr.next

        return new_list.next 
        



            
        