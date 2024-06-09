#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i<len(nums):
            m = nums[i]
            if m == val:
                i += 1
            else:
                nums[k] = m
                i += 1
                k += 1
        return k
# @lc code=end

