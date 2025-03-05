#
<<<<<<< HEAD
# @lc app=leetcode.cn id=132 lang=python3
=======
# @lc app=leetcode.cn id=132 lang=python
>>>>>>> ed1bbaed77680cc6c66799671ec10caf7f65e698
#
# [132] 分割回文串 II
#

# @lc code=start
<<<<<<< HEAD
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        dp = [[False for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] != s[j]:
                    dp[i][j] = False
                    continue
                if j - 1 >= i + 1:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = True
        
        count = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,i-1,-1):     
                if dp[i][j] == True:
                    count[i][j] = 0
                else:
                    temp_min = j - i
                    for k in range(i,j):
                        if dp[i][k] == True:
                            temp_min = min(temp_min,1+count[k+1][j])
                    count[i][j] = temp_min
                    
        
        
        # print(dp)
        # print(count)
        
        return  count[0][-1]                
        
=======
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## 看出来了，是一道dp+dfs题?试一下！
        n = len(s)
        dp = [[False for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if j - 1 >= i + 1:
                    dp[i][j] = (s[j] == s[i]) and dp[i+1][j-1]
                else:
                    dp[i][j] = (s[j] == s[i])
        result = []
        def dfs(i,path):
            if i > n-1:
                result.append(copy.copy(path))
                return
            for j in range(i,n):
                if dp[i][j]:
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
            
                
        dfs(0,[])
        res = n - 1
        for i in result:
            res = min(res,len(i)-1)    
        return res
>>>>>>> ed1bbaed77680cc6c66799671ec10caf7f65e698
# @lc code=end

