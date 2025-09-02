"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        head = reverse_list(head)

        res = 0
        index = 0
        while head:
            if head.val == 1:
                res += 2 ** index
            index += 1
            head = head.next
        
        return res