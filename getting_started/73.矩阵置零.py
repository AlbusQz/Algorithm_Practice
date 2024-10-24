#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = [False for _ in range(m)]
        cols = [False for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(m):
            if rows[i]:
                for j in range(n):
                    matrix[i][j] = 0
        
        for i in range(n):
            if cols[i]:
                for j in range(m):
                    matrix[j][i] = 0
                      
# @lc code=end