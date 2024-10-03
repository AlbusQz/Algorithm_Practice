#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        prepare = [False for _ in range(n)]
        
        for i in range(n):
            temp = nums[i]
            if temp > 0 and temp <=n:
                prepare[temp-1] = True
        
        for i in range(n):
            if prepare[i] == False:
                return i+1
            
        return n+1
            
        
# @lc code=end

