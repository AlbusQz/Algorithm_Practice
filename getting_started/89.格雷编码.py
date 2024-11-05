#
# @lc app=leetcode.cn id=89 lang=python
#
# [89] 格雷编码
#

# @lc code=start
class Solution(object):
    ## 参考了题解2
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0,1]
        base =  2
        for i in range(1,n):
            for j in range(len(result)-1,-1,-1):
                result.append(base + result[j])
            base *= 2 
        return result
        
# @lc code=end

