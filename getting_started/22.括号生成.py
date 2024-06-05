#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = ['(']
        result = []
        left = [1]
        right = [0]

        for i in range(2*n):
            m = len(strings)
            for j in range(m):
                s = strings[j]
                l = left[j]
                r = right[j]
                if l<n :
                    temps = s+'('
                    strings.append(temps)
                    if(len(temps)==2*n):
                        result.append(temps)
                    left.append(l+1)
                    right.append(r)

                if l-r > 0:
                    temps = s+')'
                    strings.append(temps)
                    if(len(temps)==2*n):
                        result.append(temps)
                    right.append(r+1)
                    left.append(l)
                    
            strings = strings[m:]
            left = left[m:]
            right = right[m:]
                   
        return result
# @lc code=end

