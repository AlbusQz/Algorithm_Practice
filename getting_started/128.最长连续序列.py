#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ## 看了题解后想到了新思路！即单向探索
        # nums = list(set(nums))
        # new_nums = []
        nums = set(nums)
        result = 0
        for i in nums:
            j = i - 1
            if j not in nums:
                j = i + 1 
                temp_l = 1
                
                while j in nums:
                    j += 1
                    temp_l += 1
                result = max(result,temp_l)
        return result
                
        
# @lc code=end

