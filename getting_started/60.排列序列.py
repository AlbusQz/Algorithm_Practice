#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        result = ""
        sons = []
        chars = []
        temp = 1
        k -= 1
        for i in range(n):
            temp *= (i+1)
            sons.append(temp)
            chars.append(i+1)
        
        i = n-2
        while i >= 0:
            print(k)
            son = sons[i]
            print(son)
            i -= 1
            index = int(k/son)
            print(index)
            k = k%son
            temp_c = chars.pop(index)
            result += str(temp_c)
        
        result += str(chars.pop())
        return result
        
        
# @lc code=end

