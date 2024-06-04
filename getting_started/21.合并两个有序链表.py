import ListNode
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        head.next = ListNode()
        i = list1
        j = list2
        n = head

        while i is not None and j is not None:
            # vali = i.val
            # valj = j.val
            # if vali < valj:
            if i.val < j.val:
                n = n.next
                # n.val = vali
                n.val = i.val
                n.next = ListNode()
                i = i.next
            else:
                n = n.next
                # n.val = valj
                n.val = j.val
                n.next = ListNode()
                j = j.next
        
        if i is not None and j is None:
            while i is not None:
                n = n.next
                n.val = i.val
                n.next = ListNode()
                i = i.next
        elif j is not None and i is None:
            while j is not None:
                n = n.next
                n.val = j.val
                n.next = ListNode()
                j = j.next

        n.next = None
        head = head.next
        return head
        
# @lc code=end

