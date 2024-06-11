#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -1*2**31:
                return 2**31-1
            else:
                return -1*dividend
        
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            flag = -1
        else:
            flag = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        stack1 = []
        stack2 = []
        times = 1
        while dividend >= divisor:
            stack1.append(times)
            stack2.append(divisor)
            times += times
            divisor += divisor
        
        
        for i in range(len(stack1)-1,-1,-1):
            if dividend>=stack2[i]:
                result += stack1[i]
                dividend -= stack2[i]
             
        return flag*result
# @lc code=end

