#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # brute force
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next
        r = len(nodes) - 1
        l = 0
        while l < r:
            if nodes[l] != nodes[r]:
                return False
            l += 1
            r -= 1
        return True
# @lc code=end

