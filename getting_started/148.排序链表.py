#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def rebuild_head(nums,left,right):
            for i in range(int((right - 1)/2),-1,-1):
                l = i *2 + 1
                if l + 1 <= right and nums[l + 1] < nums[l]:
                    temp_min = nums[l+1]
                    l += 1
                else:
                    temp_min = nums[l]
                if temp_min < nums[i]:     
                    nums[i],nums[l] = nums[l],nums[i]
            
                           
        count = {}
        vals = []
        
        while head is not None:
            val = head.val
            if val not in count:
                vals.append(head.val)
                head = head.next
                count[val] = 1
            else:
                count[val] += 1
                head = head.next
        n = len(vals)
        if n == 0:
            return head
        
        # for i in range(n-1,-1,-1):
        #     rebuild_head(vals,0,i)
        #     vals[0],vals[-(n-i)] = vals[-(n-i)],vals[0]
        vals.sort(reverse=True)
        
        result_head = ListNode(0,None)
        now_head = rebuild_head
        for i in range(1,n+1,1):
            val = vals[-i]
            temp_count = count[val]
            for j in range(temp_count):
                temp_node = ListNode(val)
                now_head.next = temp_node
                now_head = temp_node
        # return resl
            
        return rebuild_head.next
        
        
# @lc code=end

