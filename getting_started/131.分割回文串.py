#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
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
        return result
# @lc code=end

