#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = [[]]
        visited = {}
        new_nums = []
        for i in nums:
            if i not in visited:
                visited[i] = 1
                new_nums.append(i)
            else:
                visited[i] += 1
        temp = []
        m = len(new_nums)
        def dfs(index):
            
            if visited[new_nums[index]] == 0:
                return
            else:
                visited[new_nums[index]] -= 1
            temp.append(new_nums[index])
            result.append(copy.copy(temp))
            for i in range(index,m):
                # visited[i] = True
                dfs(i)
            temp.pop()
            visited[new_nums[index]] += 1
        for i in range(m):
            dfs(i)
        return result
        
# @lc code=end

