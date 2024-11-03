#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        new_head_prev = ListNode(-1)
        new_head_prev.next = None
        new_head = new_head_prev
        mid_prev = ListNode(-1)
        mid_prev.next = None
        mid = mid_prev

        
        now = head
        while now is not None:
            if now.val < x:
                new_head.next = now
                new_head = now

            else:
                mid.next = now
                mid = now
            now = now.next
        
        new_head.next = mid_prev.next
        mid.next = None
        return new_head_prev.next
            
# @lc code=end

