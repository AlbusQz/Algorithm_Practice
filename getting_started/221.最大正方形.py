#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # print(dp[0][0])
        maxArea = 0
        def extendArea(x,y):
            area = dp[x][y]
            while area > 0:
                if x + 1 >= m or y + 1 >=n or matrix[x+1][y+1] == '0':
                    area -= 1
                    continue
                flag = True
                for i in range(area):
                    if matrix[x-area+1+i][y+1] == '0' or matrix[x+1][y-area+1+i] == '0':
                        area -= 1
                        flag = False
                        break
                if flag:
                    dp[x+1][y+1] = area + 1
                    break
                else:
                    continue
            # maxArea = max(area+1, maxArea)
        
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    # maxArea = 1
        for i in range(m-1):
            for j in range(n-1):
                extendArea(i,j)
                
                # print(type(dp))
                # print(dp[i])
        
        for i in range(m):
            for j in range(n):
                maxArea = max(dp[i][j],maxArea)
        # print(dp)
        return maxArea*maxArea
        
        
        
# @lc code=end

