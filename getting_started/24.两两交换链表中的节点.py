#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head
        while n is not None:
            if n.next is None:
                break
            v1 = n.val
            n.val = n.next.val
            n.next.val = v1
            n = n.next.next
        return head
            
# @lc code=end

