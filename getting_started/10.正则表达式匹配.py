# @before-stub-for-debug-begin
from python3problem10 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #参考了这篇文章：https://blog.csdn.net/weixin_51332434/article/details/120913923
        m = len(s)+1
        n = len(p)+1
        dp = [[False for i in range(n)] for j in range(m)]
        dp[0][0] = True
        # dp[1:][0] = False
        for i in range(2,n):
            if p[i-1] == '*':
                dp[0][i] = dp[0][i-2]
        
        for i in range(1,m):
            a = i - 1
            for j in range(1,n):
                b = j - 1
                if p[b] == '*':
                    if p[b-1] == s[a] or p[b-1] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
                elif p[b] == '.' or p[b] == s[a]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        # print(dp)
        return dp[m-1][n-1]      
# @lc code=end

