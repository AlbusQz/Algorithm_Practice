#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#

# @lc code=start
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
        
# @lc code=end

