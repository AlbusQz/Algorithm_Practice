#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)]for _ in range(m)]
        nodes = []
        
        def addO(x,y,ns):
           
            if x < 0 or y < 0 or x > m-1 or y > n-1:
               return
            if visited[x][y] == True:
                return
            if board[x][y] != 'O':          
                return
            ns.append([x,y])
            visited[x][y] = True
            addO(x-1,y,ns)
            addO(x+1,y,ns)
            addO(x,y-1,ns)
            addO(x,y+1,ns)
            return 
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == False:
                    ns = []
                    addO(i,j,ns)
                    nodes.append(ns)
                
        for ns in nodes:
            flag = True
            for node in ns:
                x = node[0]
                y = node[1]
                if x == 0 or x == m-1 or y == 0 or y == n-1:
                    flag = False
                    break
            if flag == True:
                for node in ns:
                    board[node[0]][node[1]] = 'X'
        
        return           
        
# @lc code=end

