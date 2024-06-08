# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        i = 0
        former = -1*10**(4)-1
        ## better method
        while i<n:
            j = nums[i]
            if j > former:
                former = j
                nums[k] = j
                k += 1
            i += 1
        return k
    
        '''
        while i<n:
            j = nums[i]
            if j > former:
                # result.append(j)
                former = j
                i += 1
                k += 1
            else:
                nums.pop(i)
                n -= 1
        return k
        '''
# @lc code=end