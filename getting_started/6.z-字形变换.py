# @before-stub-for-debug-begin
from python3problem6 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
import math
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows <=1:
            return s
        string = []
        n  = len(s)
        Lines = 2*numRows-2
        nums = math.ceil(n/Lines)
        res = ''
        
        for i in range(numRows):
            begin = i
            if i == 0 or i == numRows-1:
                while begin < n:
                    res+=s[begin]
                    begin += Lines
            else:
                while begin < n:
                    res+=s[begin]
                    another = Lines - i + begin - i
                    if another < n:
                        res += s[another]
                    begin += Lines
        return res
                
                
            
        
# @lc code=end

