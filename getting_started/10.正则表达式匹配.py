# @before-stub-for-debug-begin
from python3problem10 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p=='.*':
            return True
        i = 0
        j = 0
        j_ = 0
        m = len(s)
        n = len(p)
        while i < m and j < n:
            if j+1<n and p[j+1] == '*':
                count = 0
                t = p[j]
                while j<n and (p[j] == '*'or p[j] == t):
                    if p[j] == t:
                        count += 1
                    else:
                        # p[j] = t
                        if j+1 <n:
                            p = p[:j]+t+p[j+1:]
                        else:
                            p = p[:j]+t
                    j += 1
                while i<m and (s[i] == t):
                    i += 1
                    count -=1

            elif s[i] != p[j] and p[j] <= 'z' and p[j] >= 'a':
                return False
            elif s[i] == p[j]:
                i += 1
                j += 1
                j_ = j
            elif p[j]=='.':
                # if j+1 <n:
                #     p = p[:j-1]+s[i]+p[j+1:]
                # else:
                #     p = p[:j-1]+s[i]
                # # p[j] = s[i]
                i += 1
                j += 1
                j_ = j
            elif p[j] =='*':
                count = 0
                t = p[j-1]
                j += 1
                
                while i<m and (s[i] == t):
                    i += 1
             
        
        if j<n or i<m :
            return False
        else :
            return True
                 
        
# @lc code=end

