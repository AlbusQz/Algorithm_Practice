#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
import math
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0:
            return 0
        #判断正负
        if x<0:
            flag = False
        else:
            flag = True
        
        x = abs(x)
        numbers = []
        result = 0
        while(x>0):
            numbers.append(x%10)
            x = x//10
        for i in range(len(numbers)):
            result += math.pow(10,i)*numbers[-(i+1)]
        if flag==False:
            result = -result
        if result<-math.pow(2,31) or result > math.pow(2,31) - 1:
            result = 0
        return int(result)
            
            
        
        
# @lc code=end

