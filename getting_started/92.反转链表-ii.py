#
# @lc app=leetcode.cn id=92 lang=python
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        hehead = ListNode(0.5)
        hehead.next = head
        flag = False
        now = head
        prev = hehead
        left_prev = hehead
        index = 0
        if left == right:
            return head
        while now is not None:
            index += 1
            if flag == False:
                if index == left:
                    flag = True
                    left_prev = prev
                    prev = now
                    left = now
                prev = now    
                now = now.next
                continue
            
            temp = now
            now = now.next
            temp.next = prev
            if index == right:
                left_prev.next = temp
                left.next = now
                break
            prev = temp
        
        return hehead.next
            
            
            
            
# @lc code=end

