#
# @lc app=leetcode.cn id=240 lang=python
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        global right_max
        right_max = m
        global down_max
        down_max = n
        global result 
        result = False
        def dfs(x,y,lastmove):
            global right_max
            global down_max
            global result 
            val = matrix[x][y]
            # print(val)
            visited[x][y] = True
            if val == target:
                result = True
                
            elif val < target:
                if x+1 < right_max and visited[x+1][y] == False:
                    dfs(x+1,y,0)
                if y + 1 < down_max and visited[x][y+1] == False:
                    dfs(x,y+1,1)
            # else:
            #     if lastmove == 0:
            #         right_max = min(right_max,x+1)
            #     elif lastmove == 1:
            #         down_max = min(down_max,y+1)
            return
        
        dfs(0,0,-1)
        return result
# @lc code=end

