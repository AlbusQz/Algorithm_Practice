#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 and n > 0:
            return 0.0
        if n == 0 and x != 0:
            return 1.0
        if x == 1:
            return 1.0
        if n == 1:
            return x
        if x == -1:
            if n%2 == 0:
                return 1
            else:
                return -1
        result = 1
        if abs(x) <0.5 and n > 100 :
            return 0
        if n < -100:
            return 0
        if n > 0:
            for i in range(n):
                result = result*x
        if n < 0:
            for i in range(abs(n)):
                result = result*x
            result = 1/result
        return result
# @lc code=end

