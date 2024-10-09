#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isvalid(board,x,y):
            # check row
            for i in range(n):
                if i == y:
                    continue
                elif board[x][i] == 'Q':
                    return False
            
            # check column
            for i in range(n):
                if i == x:
                    continue
                elif board[i][y] == 'Q':
                    return False
            
            # check diagonal
            i = x + 1
            j = y + 1
            while i<n and j <n:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j += 1
            
            i = x + 1
            j = y - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1
            
            i = x - 1
            j = y + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            i = x - 1
            j = y - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Arriving here means this board is valid.
            return True
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []
        ## 注意，visited数组在本题中用不上
        # visited = [[False for _ in range(n)] for _ in range(n)]

        def dfs(m):
            if m == n:
                temp = []
                for s in board:
                    temp.append("".join(s))
                result.append(temp)
                return 
            for i in range(n):
                if isvalid(board,m,i):
                    board[m][i] = 'Q'
                    # visited[m][i] = True
                    dfs(m+1)
                    board[m][i] = '.'
                    # visited[m][i] = False
        dfs(0)
        return result
            
            
# @lc code=end

