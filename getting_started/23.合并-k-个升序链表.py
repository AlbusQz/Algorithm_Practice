#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
import ListNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        for i in range(0,n-1):
            j = i + 1
            p1 = lists[i]
            p2 = lists[j]
            head = ListNode()
            p = head
            while p1 is not None and p2 is not None:
                if p1.val < p2.val:
                    p.next= p1
                    p = p.next
                    p1 = p1.next
                else:
                    p.next = p2
                    p = p.next
                    p2 = p2.next
            
            if p1 is not None and p2 is None:
                while p1 is not None:
                    p.next = p1
                    p = p.next
                    p1 = p1.next
            else:
                while p2 is not None:
                    p.next = p2
                    p = p.next
                    p2 = p2.next 
            lists[j] = head.next
        return lists[-1]
            
                    
# @lc code=end

