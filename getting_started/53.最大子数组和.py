#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = []
        n = len(nums)
        maxSum.append(nums[0])
        for i in range(n-1):
            if maxSum[-1]>0:
                maxSum.append(maxSum[-1] + nums[i+1])
            else:
                maxSum.append(nums[i+1])
        return max(maxSum)
# @lc code=end

