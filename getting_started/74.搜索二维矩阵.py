#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m
        mid = int((left + right)/2)
        
        while left < right - 1:
     
            mid = int((left + right)/2)
            if matrix[mid][0] > target:
                right = mid
            elif matrix[mid][-1] < target:
                left = mid
            else:
                break
        mid = int((left + right)/2)
        
        left = 0
        right = n
        mid2 = int((left + right)/2)
        while left < right - 1:
            mid2 = int((left + right)/2)
            if matrix[mid][mid2] > target:
                right = mid2
            elif matrix[mid][mid2] < target:
                left = mid2
            else:
                return True
        mid2 = int((left + right)/2)
        if matrix[mid][mid2] == target:
            return True
        return False
        
        
# @lc code=end

