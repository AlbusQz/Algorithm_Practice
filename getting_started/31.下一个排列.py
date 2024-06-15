# @before-stub-for-debug-begin
from python3problem31 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #with help:https://leetcode.cn/problems/next-permutation/solutions/80560/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
        n = len(nums)
        if n == 1:
            return 
        elif n == 2:
            nums[0],nums[1] = nums[1],nums[0]
            return 
        i = n-2
        j = n-1
        
        while i>=0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        value = nums[i]
        
        if i>= 0:
            while j>i:
                if nums[j]>value:
                    break
                j -= 1
            
            nums[i],nums[j] = nums[j],nums[i]
            
        i += 1
        j = n-1
        while j>i:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        return
        
# @lc code=end

