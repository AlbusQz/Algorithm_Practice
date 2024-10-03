#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ##用来负数的方式做标记，很巧妙，就可以避免标记带来的信息丢失
        
        n = len(nums)
        
        for i in range(n):
                if nums[i]<=0 :
                    nums[i] = n+1 
        
        for i in range(n):
            temp = abs(nums[i])
            if temp <= n:
                nums[temp-1] = - abs(nums[temp-1])
        
        for i in range(n):
            if nums[i]>0:
                return i+1
            
        return n+1
                
        
        ## 看错要求了，要求o(1)的空间复杂度，我用了o(n)的
        '''
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
        '''
            
        
# @lc code=end

