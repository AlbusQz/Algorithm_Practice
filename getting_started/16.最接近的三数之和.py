# @before-stub-for-debug-begin
from python3problem16 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[n-1]
        min_ = abs(result-target)
        for i in range(0,n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            
            ## better method  by 灵茶山艾府
            ## https://leetcode.cn/problems/3sum-closest/solutions/2337801/ji-zhi-you-hua-ji-yu-san-shu-zhi-he-de-z-qgqi/

            x = nums[i]
            #优化一
            temp = x+nums[i+1]+nums[i+2]
            if temp > target:
                if abs(temp-target)<min_:
                   return temp
            
            #优化二
            
            temp = x+nums[-1]+nums[-2]
            if temp < target:
                if abs(temp-target)<min_:
                    min_ = abs(temp-target)
                    result = temp
                continue
            ## ending method
            
            while j<k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return target
                if abs(temp-target)<min_:
                    min_ = abs(temp-target)
                    result = temp
                if temp < target:
                    former = nums[j]
                    j += 1
                    while j<k and nums[j] == former:
                        j += 1
                else:
                    former = nums[k]
                    k -= 1
                    while k>j and nums[k] == former:
                        k -= 1           
                                       
        return result
# @lc code=end

