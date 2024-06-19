#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        n = len(nums)
        i = 0
        j = n-1
        
        if n == 0:
            return result
        
        if n == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return result
        
        if target < nums[0] and target > nums[j]:
            return result
        
        flag = False
        
        while i<=j:
            mid = int((i+j)/2)
            if nums[mid] == target:
                flag = True
                i = mid
                j = mid
                break
            
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        if not flag:
            return result
        
        
        while i > 0 and nums[i-1] == target:
            i -= 1
        
        while j < n-1 and nums[j+1] == target:
            j += 1
        
        return [i,j]
                
# @lc code=end

