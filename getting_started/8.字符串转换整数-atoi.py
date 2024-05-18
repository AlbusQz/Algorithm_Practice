# @before-stub-for-debug-begin
from python3problem8 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
import math
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        # m = 0
        #
        if len(s) == 0:
            return 0
        
        while s[0] == ' ' and len(s)>1:
            s = s[1:]
        
        m = i
        
        if s[0] == '-' and len(s)>1:
            flag = True
            s = s[1:]
        elif s[0] == '+'  and len(s)>1:
            flag = False
            s = s[1:]
        else:
            flag = False

        result = 0
        n = len(s)
        j = 0
        while j < n and s[j] >= '0' and s[j] <= '9':
            j += 1
            
        while i<j and result <= pow(2,31):
            if s[i]<'0' or s[i]>'9':
                if flag:
                    result = -result
                return result
            elif m==0 and s[i]=='0':
                i += 1
            else:
                result += int(s[i])*pow(10,j-i-1)
                i += 1
                # m += 1
        if result >= pow(2,31):
            if flag:
                result = -pow(2,31)
            else:
                result = pow(2,31)-1
        else:
            if flag:
                result = -result
        return result             
# @lc code=end

