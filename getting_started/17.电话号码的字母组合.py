#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        n = len(digits)
        if n == 0:
            return []
        result = ['']
        i = 0
        while i < n:
            temp_result = []
            letters = num_to_letters[digits[i]]
            for l in letters:
                for r in result:
                    temp_result.append(r+l)
            result = temp_result
            i += 1
        return result          
# @lc code=end

