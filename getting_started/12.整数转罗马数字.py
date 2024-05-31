# @before-stub-for-debug-begin
from python3problem12 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        tens = ['I','X','C','M']
        fives = ['V','L','D']
        result = ''
        # nums = []
        i = 0
        while num > 0 :
            n = num%10
            if n < 4:
                for j in range(n):
                    result = tens[i] + result
            elif n == 4:
                result = tens[i] + fives[i] + result 
            elif n == 5:
                result = fives[i] + result
            elif n > 5 and n < 9:
                for j in range(n-5):
                    result = tens[i] + result
                result = fives[i] + result
            else:
                result = tens[i] + tens[i+1] + result
            num = num // 10
            i = i + 1
        return result
                
                
                    
            
# @lc code=end

