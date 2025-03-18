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
        '''
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
        '''
        ### 反向列表法，时间o(m+n)，空间o(1)
        ### 不得行，不能修改链表结构/(ㄒoㄒ)/~~
        '''
        a = headA
        pre = None
        while a is not None:
            temp = a.next
            a.next = pre
            pre = a
            a = temp
        headA = pre
        
        b = headB
        pre = None
        while b is not None:
            temp = b.next
            b.next = pre
            pre = b
            b = temp
        headB = pre
        
        begin = None
        while headA == headB:
            begin = headA
            headA = headA.next
            headB = headB.next
        return begin
        '''
        ### 测长度法，时间o(m+n)，空间o(1)
        a = headA
        m = 0
        while a is not None:
            a = a.next
            m += 1
        
        b = headB
        n = 0
        while b is not None:
            b = b.next
            n += 1

        a = headA
        b = headB
        if m > n:
            for _ in range(m-n):
                a = a.next
        else:
            for _ in range(n-m):
                b = b.next
        
        while a is not None and b is not None:
            if a == b:
                return a
            a = a.next
            b = b.next
        
        return None
         
# @lc code=end

