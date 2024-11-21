#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        ns = []
        temp_n = 1
        dp = copy.copy(triangle)
        dp[0][0] = triangle[0][0]
        n = 2
        for i in range(1,m):
            for j in range(n):
                if j > 0 and j < n - 1:

                    dp[i][j] += min(dp[i-1][j-1],dp[i-1][j])

                elif j == 0:
                    dp[i][j] += dp[i-1][0]
                else:
                    dp[i][j] += dp[i-1][j-1]
            n += 1
        # print(dp)
        return min(dp[-1])
# @lc code=end

