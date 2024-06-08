#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

import ListNode

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = head
        while n is not None:
            m = n
            i = 0
            lists = []
            
            while i<k and m is not None:
                lists.append(m.val)
                m = m.next
                i += 1
                
            if i<k:
                break
            
            for j in range(i):
                n.val = lists[-(j+1)]
                n = n.next
                
        return head
            
            
# @lc code=end

