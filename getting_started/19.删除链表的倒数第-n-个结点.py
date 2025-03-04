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
        pointer = head
        remove_pointer = head
        
        while i < n :
            remove_pointer = remove_pointer.next
            i += 1
        if remove_pointer is None:
            return head.next
        
        while remove_pointer.next is not None:
            remove_pointer = remove_pointer.next
            pointer = pointer.next
        
        pointer.next = pointer.next.next
        return head
        
        
            
# @lc code=end

