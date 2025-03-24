#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        ## 经典dp题
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            if dp[i-1] == dp[i-2]:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        
# @lc code=end

