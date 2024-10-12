#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  
        ## 排列组合法
        '''
        top = m + n - 2
        bottom = 1
        result = 1
        for i in range(min(m,n)-1):
            result *= top
            result /= bottom
            top -= 1 
            bottom +=1
        return int(result)
        '''
        ## 看了题解后知道有的dp法，dp[i][j] = dp[i-1][j] + dp[i][j-1]
        ## 即到达一个位置的路径数量等于到他上面和左面的位置的路径数量的和
        dp = [[0 for _ in range(n)]for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i >= 1:
                    dp[i][j] += dp[i-1][j]
                if j >= 1:
                    dp[i][j] += dp[i][j-1]
        # print(dp)
        return dp[-1][-1]
        
    
# @lc code=end

