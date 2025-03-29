#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        ## space complexity = O(1):
        n = len(nums)
        result = [1]
        
        for i in range(n-1):
            result.append(result[-1]*nums[i])
        
        r = 1
        for i in range(n-1,-1,-1):
            result[i] = r * result[i]
            r = r * nums[i]
        
        return result
    
        ## space complexity = O(n):
        '''
        n = len(nums)

        left = [1]
        right = [1]
        result = []
        
        for i in range(n-1):
            left.append(left[-1] * nums[i])
            right.insert(0,right[0] * nums[n-1-i])
        
        for i in range(n):
            result.append(left[i] * right[i])
        
        return result
        '''
    
# @lc code=end

