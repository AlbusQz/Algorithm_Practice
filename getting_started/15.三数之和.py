# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ##
        
        ## brute force
        '''
        hashtable = set()
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            for j in range(i+1,n):
                num2 = nums[j]
                for k in range(j+1,n):
                    num3 = nums[k]
                    if num1+num2+num3==0:
                        l = [num1,num2,num3]
                        l.sort()
                        hashtable.add(tuple(l))
        result = list(hashtable)
        return result
        '''
# @lc code=end
        
