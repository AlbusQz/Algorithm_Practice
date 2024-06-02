#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # num_of_letter = [3,3,3,3,3,4,3,4]
        # num_of_letter = {
        #     '2':3,
        #     '3':3,
        #     '4':3,
        #     '5':3,
        #     '6':3,
        #     '7':4,
        #     '8':3,
        #     '9':4,
        # }
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
        # length = 1
        # lengths = []
        
        # for s in digits:
        #     lengths.append(length)
        #     length = length * num_of_letter[s]
            
        
        # result = ['' for i in range(length)]
        # # i = 0
        # for i,s in enumerate(digits):
        #     length
        #     for j in num_to_letters[s]:
                
                
            
# @lc code=end

