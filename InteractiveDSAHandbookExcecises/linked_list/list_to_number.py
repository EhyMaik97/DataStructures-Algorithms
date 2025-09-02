"""
Exercise only on the book not on Leetcode
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def get_decimal_value(self, head: Optional[ListNode]) -> int:
        
        res = 0
        while head:
            res = res*10 + head.value
            head = head.next
        return res