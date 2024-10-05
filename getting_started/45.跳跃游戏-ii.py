#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0:
            return 0
        i = n-1
        step = 0
        
        while i>0:
            for j in range(0,i):
                if j + nums[j] >= i:
                    i = j
                    break
            step += 1
        return step
        
            
        
# @lc code=end

