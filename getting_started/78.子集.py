#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [[]]
        n = len(nums)
        visited = [False for _ in range(n)]
        temp = []
        def dfs(i):
            if i >= n:
                return 
            if visited[i] == True:
                return 
            temp.append(nums[i])
            visited[i] = True
            result.append(copy.copy(temp))
            j = i + 1
            while j < n:
                dfs(j)
                j += 1
            temp.pop()
            visited[i] = False
        for i in range(n):
            dfs(i)
        return result
        
# @lc code=end

