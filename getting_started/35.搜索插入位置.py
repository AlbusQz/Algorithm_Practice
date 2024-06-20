#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if n == 1:
            if nums[0] <target:
                return 1
            else:
                return 0
        
        i = 0
        j = n-1
        flag = 0
        
        while i<=j:
            mid = int((i+j)/2)
            if nums[mid] == target:
                flag = 0
                break
            if nums[mid] < target :
                i = mid + 1
                flag = 1
            else:
                j = mid - 1
                flag = 0

        return mid+flag
            
        
# @lc code=end

