# @before-stub-for-debug-begin
from python3problem9 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # using int only
        '''
        y = 0
        _ = x
        while x > 0:
            y = 10*y + x%10
            x = x//10
        return y==_
        '''
        #using string
        x = str(x)
        n = len(x)
        i = 0
        j = n-1
        while i <= j:
            if x[i]!=x[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
# @lc code=end

