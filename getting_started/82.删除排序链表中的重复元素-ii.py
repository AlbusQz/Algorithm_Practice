#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
        
        headhead = ListNode(-1)
        headhead.next = head
        prev = headhead
        left = head
        right = head.next
        
        while left is not None:
            
            if right is not None and left.val == right.val:
                
                val = left.val
                left = right
                while left is not None and left.val == val:
                    left = left.next
                prev.next = left
                if left is not None:
                    right = left.next
                    continue
                else:
                    break
                
            if right is None:
                break
            
            prev = left
            left = right
            right = right.next
        
        return headhead.next
        
# @lc code=end

