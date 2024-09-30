# @before-stub-for-debug-begin
from python3problem38 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
'''
迭代法
'''
class Solution:
    def RLE(self,rle):

        n = len(rle)
        result = ''

        same = 0
        i = 0
        while i < n-1:
            if rle[i] == rle[i+1]:
                i += 1
                same += 1
                continue
            else:
                result += str(same+1)
                result += rle[i]
                same = 0
                i += 1
            
        if rle[i] == rle[i-1]:
            result += str(same+1)
            result += rle[i]
        else:
            result += '1'
            result += rle[i]
            
        return result 
            
        
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        result = '1'
        for i in range(n-1):
            result = self.RLE(result)
        return result

'''
递归法 
class Solution:
    def RLE(self,rle):

        n = len(rle)
        result = ''

        same = 0
        i = 0
        while i < n-1:
            if rle[i] == rle[i+1]:
                i += 1
                same += 1
                continue
            else:
                result += str(same+1)
                result += rle[i]
                same = 0
                i += 1
            
        if rle[i] == rle[i-1]:
            result += str(same+1)
            result += rle[i]
        else:
            result += '1'
            result += rle[i]
            
        return result 
            
        
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.RLE(self.countAndSay(n-1))
'''
# @lc code=end

