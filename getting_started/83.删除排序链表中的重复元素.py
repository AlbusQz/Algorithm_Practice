#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        left = head
        right = left.next
        
        while right is not None:
            
            if right.val == left.val:
                right = right.next
                left.next = right
                continue
            left = right
            right = right.next
        
        return head
# @lc code=end

