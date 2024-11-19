#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex + 1
        if numRows == 1:
            return [1]
        if numRows == 2:
            return [1,1]
        result = [[1],[1,1]]
        for i in range(3,numRows+1):
            temp_result = [1]
            for j in range(i - 2):
                temp_result.append(result[i-2][j]+result[i-2][j+1])
            temp_result.append(1)
            result.append(temp_result)
        return result[-1]
        
# @lc code=end

