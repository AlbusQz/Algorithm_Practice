#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        ## less space opacity
        n = len(nums)
        for i in nums:
            val = (i-1)%(n)
            print(val)
            nums[val] += n
                
        result = []
        for i in range(n):
            if nums[i]-1 <n:
                result.append(i+1)
        
        
        
        return result
        
        ## brute force:
        '''
        n = len(nums)
        flag = [False for _ in range(n)]
        for i in nums:
            flag[i-1] = True
        result = []
        for i in range(n):
            if flag[i] == False:
                result.append(i+1)
        return result
        '''
# @lc code=end

