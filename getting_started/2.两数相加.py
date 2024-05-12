#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#
import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_node = ListNode(0)
        second_node = ListNode(0)
        last_node = None
        # first_node.next = second_node
        head = first_node
        while(l1 or l2):
            if l1:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            temp_val = first_node.val + a + b
            if temp_val >= 10:
                temp_val = temp_val%10
                second_node.val +=1
            first_node.val = temp_val
            first_node.next = second_node
            last_node = first_node
            first_node = second_node
            second_node = ListNode(0)
        if last_node.next and last_node.next.val==0:
            last_node.next = None
        return head
            
                
            
        
# @lc code=end

