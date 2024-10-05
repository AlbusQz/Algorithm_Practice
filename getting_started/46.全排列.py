#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #递归回溯法，注意copy的使用
        '''
        def dfs(depth,n,nums,used,path):
            
            if depth == n:
                print(path)
                result.append(copy.copy(path))                
                # return path
            
            for i in range(n):
                if used[i] == False:
                    path.append(nums[i])
                    used[i] = True
                    dfs(depth+1,n,nums,used,path)
                    # print(result)
                    used[i] = False
                    path.pop()
            
            return
            
        n = len(nums)
        
        path = []
        used = [False for _ in range(n)]
        result = []
        dfs(0,n,nums,used,path) 

        return result
        '''
        
        
        #暴力存储法
        '''
        result = []
        n = len(nums)
        
        list_a = []
        list_b = []
        
        for i in range(n):
            temp = copy.copy(nums)
            list_a.append([temp.pop(i)])
            list_b.append(temp)
        
        for l in range(n-1):
            a_temp = []
            b_temp = []
            for i in range(len(list_a)):
                a = list_a[i]
                b = list_b[i]
                for j in range(len(b)):
                    temp_a = copy.copy(a)
                    temp_b = copy.copy(b)
                    temp_a.append(temp_b.pop(j))
                    a_temp.append(temp_a)
                    b_temp.append(temp_b)
            del(list_a)
            del(list_b)
            list_a = a_temp
            list_b = b_temp
        return list_a                    
        '''
        
        
# @lc code=end

