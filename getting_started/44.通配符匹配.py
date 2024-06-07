#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)+1
        n = len(p)+1
        
        dp = [[False for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = True
        
        for i in range(1,n):
            if p[i-1]=='*':
                dp[0][i] = True
            else:
                break
                
        for i in range(1,m):
            a = i-1
            for j in range(1,n):
                b = j-1
                if p[b]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif s[a] == p[b] or p[b] == "?":
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return dp[m-1][n-1]
        
# @lc code=end

