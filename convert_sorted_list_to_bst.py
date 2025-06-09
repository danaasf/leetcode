# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

from typing import Optional
from leetcode.balanced_binary_tree import TreeNode
from leetcode.linked_list_cycle import ListNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def helper(head, tail):
            if head == tail:
                return None

            node = getMid(head, tail)
            root = TreeNode(node.val)
            root.left = helper(head, node)
            root.right = helper(node.next, tail)
            node.next = None

            return root

        def getMid(head, tail):
            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next
            return slow

        return helper(head, None)
