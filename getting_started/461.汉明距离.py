#
# @lc app=leetcode.cn id=461 lang=python
#
# [461] 汉明距离
#

# @lc code=start
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # def 
        if x < y:
            x, y = y, x
        xs = []
        ys = []
        while x > 0 :
            xs.append(x%2)
            x = x >> 1
        m = len(xs)
        
        while y > 0:
            ys.append(y%2)
            y = y >> 1
        n = len(ys)
        for i in range(m - n):
            ys.append(0)
        # print(xs)
        # print(ys)
        result = 0
        for i in range(m):
            result += (xs[i] != ys[i])
        
        return result
        
# @lc code=end

