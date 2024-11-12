#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            p = 0
            q = i - 1
            while p < i:
                dp[i] += dp[p]*dp[q]
                p += 1
                q -= 1
        
        return dp[n]
# @lc code=end

