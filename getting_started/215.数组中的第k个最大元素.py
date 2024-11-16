#
# @lc app=leetcode.cn id=215 lang=python
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution(object):
    
    ## 堆排序法
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def rebulid_Tree(nums,left,right):
            if left == right:
                return
            before = left
            i = 2 * left + 1
            while i < right:
                if i + 1 < right and nums[i+1] > nums[i]:
                    i += 1
                if nums[before] >= nums[i]:
                    break
                nums[before],nums[i] = nums[i],nums[before]
                before = i
                i = i * 2 +1
        
        n = len(nums)
        m = int(n/2)
        for i in range(m,-1,-1):
            rebulid_Tree(nums,i,n)
        for i in range(k):
            nums[0],nums[-1-i] = nums[-1-i],nums[0]
            rebulid_Tree(nums,0,n-1-i)
        return nums[-k]
            
# @lc code=end

