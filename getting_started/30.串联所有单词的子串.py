# @before-stub-for-debug-begin
from python3problem30 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #又是一道滑动窗口
        hashset1 = {}
        result = []
        
        m = len(words)
        n = len(words[0])
        mn = m*n
        for word in words:
            if word in hashset1:
                hashset1[word] += 1
            else:
                hashset1[word] = 1
        

        for i in range(0,len(s)-mn+1):
            hashset2 = hashset1.copy()
            for j in range(i,i+mn,n):
                t = s[j:j+n]
                if t not in hashset2:
                    break
                else:
                    hashset2[t] -= 1
                    if hashset2[t] == 0:
                        hashset2.pop(t)
            if len(hashset2) == 0:
                result.append(i)
        return result           
# @lc code=end

