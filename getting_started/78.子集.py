#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        #迭代法
        result = [[]]
       
        n = len(nums)
        stack = [[i] for i in nums]
        index = [i for i in range(n)]
        
        while len(stack)>0:
            temp = stack.pop()                                
            result.append(copy.copy(temp))
            temp_index = index.pop()
            for i in range(temp_index+1,n):
                temp_2 = copy.copy(temp)
                temp_2.append(nums[i])
                stack.append(temp_2)
                index.append(i)
        
        return result
        #递归法
        '''
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
        '''
        
# @lc code=end

