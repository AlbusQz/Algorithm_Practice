# @before-stub-for-debug-begin
from python3problem13 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        
        value_dict = {
            'I':1,
            'X':10,
            'C':100,
            'M':1000,
            'V':5,
            'L':50,
            'D':500
        }
        n = len(s)
        
        i = 0
        
        while i < n:
            t = s [i]
            v = value_dict[t]
            if i+1 <n:   
                t_ = s[i+1]
                
                v = value_dict[t]
                v_ = value_dict[t_]
                
                if t == t_:
                    while i<n and s[i] == t:
                        result += v
                        i = i + 1 
                elif v_/v==5 or v_/v ==10:
                    result = result + (v_-v)
                    i = i + 2
                else:
                    result = result + v
                    i = i + 1
            else:
                return result + v  
        return result
            
# @lc code=end

