#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast = head
        slow = head
        # flag = False
        while fast is not None:
            fast = fast.next
            slow = slow.next
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            if fast == slow:
                # flag = True
                break
        
        while head != slow:
            head = head.next
            slow = slow.next
        return head
        
# @lc code=end

