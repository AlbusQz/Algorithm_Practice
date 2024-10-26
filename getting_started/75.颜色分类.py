#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        r = 0
        w = 0
        b = 0
        
        for i in nums:
            if i == 0:
                r += 1
            elif i == 1:
                w += 1
            elif i ==2:
                b += 1

        index = 0
        
        for i in range(r):
            nums[index + i] = 0

        index += r
        
        for i in range(w):
            nums[index + i] = 1
        
        index += w
        
        for i in range(b):
            nums[index + i] = 2
        
 
# @lc code=end

