# @before-stub-for-debug-begin
from python3problem32 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        flags = [False for _ in range(n)]
        
        stack = []
        index = []
        
        result = 0
        top = -1
        for i in range(n):
            if s[i] == '(':
                stack.append('(')
                index.append(i)
                top += 1
                # index += 1
            elif s[i] == ')':
                if top>=0 and stack[top] == '(':
                    stack.pop()
                    temp_index = index.pop()
                    flags[i] = True
                    flags[temp_index] = True

                    top -= 1
        
        temp_result = 0
        for i in range(n):
            if flags[i] == True:
                temp_result += 1
                result = max(result,temp_result)
            else:
                temp_result = 0
        return result
# @lc code=end

