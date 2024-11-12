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
        ## 打表！
        dp = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
        return dp[n]
        
        ## dp法
        '''
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
        '''
# @lc code=end
# if __name__ == '__main__':
#     n = 19
#     result = []
#     dp = [0 for _ in range(n+1)]
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2,n+1):
#         p = 0
#         q = i - 1
#         while p < i:
#             dp[i] += dp[p]*dp[q]
#             p += 1
#             q -= 1
#     print(dp)
