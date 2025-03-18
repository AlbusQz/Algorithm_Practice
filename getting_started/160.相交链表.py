#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ### 散列法，时间o(m+n)，空间o(m)
        nodes_dict = {}
        a = headA
        i = 0
        while a is not None:
            nodes_dict[a] = i
            i += 1
            a = a.next
        
        b = headB
        begin = None
        while b is not None:
            if b in nodes_dict:
                begin = b
                break
            b = b.next
        return begin
        
# @lc code=end

