#
# @lc app=leetcode.cn id=36 lang=python
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        set1 = set()
        set2 = set()
        set3 = set()
        ## check row and column data:
        for i in range(9):
            
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in set1:
                        return False
                    else:
                        set1.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in set2:
                        return False
                    else:
                        set2.add(board[j][i])
                        
            set1.clear()
            set2.clear()
        
        ## check the area:
        x = -3
        y = 0
        for k in range(9):
            x += 3
            if x == 9:
                x = 0
                y += 3
            for i in range(3):
                for j in range(3):
                    if board[x+i][y+j] != '.':
                        if board[x+i][y+j] in set3:
                            return False
                        else:
                            set3.add(board[x+i][y+j])
            
            set3.clear()
        
        return True
# @lc code=end

