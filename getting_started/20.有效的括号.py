#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # top = 0
        left = ['(','[','{']
        right = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        for t in s:
            if t in left:
                stack.append(t)
                # top += 1
            else:
                if len(stack) == 0:
                    return False
                t_ = right[t]
                if stack[-1] == t_:
                    stack.pop(-1)
                    # top
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
        
# @lc code=end

