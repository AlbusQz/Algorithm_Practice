# @before-stub-for-debug-begin
from python3problem28 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        
        m = len(haystack)
        n = len(needle)
        next = [0 for _ in range(n)]
        
        next[0] = 0
        i = 0
        for j in range(1,n):
            if needle[i] == needle[j]:
                next[j] = i+1
                i += 1
            else:
                while needle[i] != needle[j] and i != 0:
                    i = next[i-1]
                if i == 0:
                    if needle[i] != needle[j]:
                        next[j] = 0
                    else:
                        next[j] = 1
                        i += 1
                else:
                    next[j] = i+1
                    i += 1
                    
        j = 0
        for i in range(0,m):
            while j!=0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i+1-n
        
        if j != n:
            return -1
        else:
            return (i+1-n)
        
# @lc code=end

