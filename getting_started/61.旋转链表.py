#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head is None:
            return head
        n = 0
        pointer = head
        while pointer.next is not None:
            n += 1
            pointer = pointer.next
        if n == 0:
            return head
        pointer.next = head
        k = k % (n+1)
        print(k)
        new_pointer = head
        for i in range(n-k):
            new_pointer = new_pointer.next
               
        result = new_pointer.next
        new_pointer.next = None
        return result
        

        
# @lc code=end

