#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## 看完solution明白使用dp法
        
        M = 10** 9 + 7

        m = len(s)
        n = len(t)
        
        dp = [[0 for _ in range(n+1 )] for _ in range(m +1 )]
        for i in range(n + 1):
            dp[0][i] = 0
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        
        return dp[m][n] % M
                
        
             
        
# @lc code=end

