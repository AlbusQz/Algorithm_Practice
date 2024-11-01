#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        n = len(nums)
        begin = nums[0]
        if target == begin:
            return True
        elif target > begin:
            i = 1
            while i < n and nums[i] < target:
                i += 1
            if i < n and nums[i] == target:
                return True
        else:
            i = 1
            while i < n and nums[i] > target:
                i += 1
            while i < n and nums[i] < target:
                i += 1
            if i < n and nums[i] == target:
                return True
        
        return False
        
# @lc code=end

