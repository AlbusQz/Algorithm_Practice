#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        m = len(nums)
        nums.sort()
        nums_set = {}
        # before = nums[0]
        # count = 0
        nums_unique = []
        for i in nums:
            if i in nums_set:
                nums_set[i] += 1
            else:
                nums_set[i] = 1
                nums_unique.append(i)
        
        n = len(nums_unique)
        
        # visited = [False for _ in range(n)]
        result = []
        path = []
        
        def dfs(depth):
            
            if depth == m:
                result.append(copy.copy(path))
                return
            
            for i in range(n):
                num = nums_unique[i]
                if nums_set[num]>0:
                    nums_set[num] -= 1
                    path.append(num)
                    dfs(depth+1)
                    nums_set[num] += 1
                    path.pop()
        
        dfs(0)
        return result
        
        
# @lc code=end

