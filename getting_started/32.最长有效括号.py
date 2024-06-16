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
        
        def my_method(s):
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
        
        #adding dp method
        def dp_method(s):
            
            n = len(s)
            if n == 0:
                return 0
            dp = [0 for _ in range(n)]
            for i in range(1,n):
                if s[i] == ')':
                    if s[i-1]== '(':
                        if i-2 >=0:
                            dp[i] = dp[i-2] + 2
                        else:
                            dp[i] = 2
                    else:
                        if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                            if i-dp[i-1]-2 >= 0:
                                dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                            else:
                                dp[i] = dp[i-1]+2
            # print(dp)
            return max(dp)
            
        return dp_method(s)
# @lc code=end

