# @before-stub-for-debug-begin
from python3problem37 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def update_Cube(board,cubes,row,col):
            
            index = int(board[row][col]) - 1
            mul_row = int(row/3)
            mul_col = int(col/3)
            count = 0
            
            for r in range(9):
                cubes[r][col][index] = False
            count = 0

            
            for c in range(9):
                cubes[row][c][index] = False
            count = 0

            for r in range(3):
                for c in range(3):
                    cubes[r+mul_row*3][c+mul_col*3][index] = False
            count = 0

        def count_Cube(cubes,row,col):
            cube = cubes[row][col]
            count = 0
            index = -1
            for i in range(9):
                if cube[i] == True:
                    count += 1
                    index = i+1
            if count != 1:
                index = -1
            return index
        
        empty_cube = [True for _ in range(9)]
        full_cube = [False for _ in range(9)]
        cubes = []
        cube_count = 0
        
        for row in range(9):
            row_cubes = []
            for col in range(9):
                if board[row][col] == '.':
                    row_cubes.append(empty_cube.copy())
                    cube_count += 1
                else:
                    row_cubes.append(full_cube.copy())
            cubes.append(row_cubes)

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    update_Cube(board,cubes,row,col)
        
        while cube_count > 0:
            
            for row in range(9):
                for col in range(9):
                    if cubes[row][col] != '.':
                        index = count_Cube(cubes,row,col)
                        if index > 0:
                            board[row][col] = str(index)
                            cubes[row][col] = full_cube.copy()
                            update_Cube(board,cubes,row,col)
                            cube_count -= 1
        
        # print(board)       
# @lc code=end

