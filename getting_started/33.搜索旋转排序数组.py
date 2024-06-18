#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#
# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 1.find the turn point
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        if n == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
                
        head = nums[0]
        i = 0
        j = n-1
        mid = 0
        flag = False
        while i<j:
            mid = int((i+j)/2)
            if nums[mid]> nums[mid+1]:
                flag = True
                break
            if nums[mid] < nums[mid-1]:
                flag = True
                mid -= 1
                break
            
            if nums[mid] > head:
                i = mid + 1
            else:
                j = mid - 1 
        
        if not flag:
            mid = -1
        # print(mid)
        if mid >= 0:
            right = nums[mid]
            left = nums[mid+1]
            if target == head:
                return 0
            elif target == left:
                return mid+1
            elif target == right:
                return mid
            elif target < left or target > right:
                return -1
            elif target > left and target < head:
                i = mid+1
                j = n-1
            else:
                i = 0
                j = mid-1
        else:
            
            right = nums[-1]
            left = nums[0]
            if target == left:
                return 0
            elif target == right:
                return n-1
            elif target < left or target > right:
                return -1
            i = 0
            j = n-1
        ## 2.find the target
        
        

        
        while i<=j:
            mid = int((i+j)/2)
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid -1
        
        return -1
             
        
        
# @lc code=end

