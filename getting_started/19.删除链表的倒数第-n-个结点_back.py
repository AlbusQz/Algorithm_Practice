# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        former = head
        now = head
        while i < n:
            now = now.next
            i += 1
        if now is None:
            return head.next
        else:
            while now.next is not None:
                now = now.next
                i += 1
                former = former.next
            former.next = former.next.next
        return head
            
            
# @lc code=end

