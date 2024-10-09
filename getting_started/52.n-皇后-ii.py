#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:

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
        res= 0

        def dfs(m):
            nonlocal res
            if m == n:
                res += 1
                return 1
            for i in range(n):
                if isvalid(board,m,i):
                    board[m][i] = 'Q'
                    dfs(m+1)
                    board[m][i] = '.'
            return 0
        print(dfs(0))
        return res

# @lc code=end

