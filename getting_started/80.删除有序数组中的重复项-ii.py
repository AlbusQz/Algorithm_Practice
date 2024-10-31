#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set0 = set()
        set1 = set()
        n = len(nums)
        i = 0
        while i < n:
            temp = nums[i]
            if temp not in set0:
                set0.add(temp)
            elif temp not in set1:
                set1.add(temp)
            else:
                nums.pop(i)
                n -= 1
                continue
            i += 1
# @lc code=end

