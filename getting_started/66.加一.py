#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        i = n-1
        result = []
        # temp = 1
        while i >= 0:
            num = digits[i]
            i -= 1
            if num + 1 >= 10:
                num = 0
                result.insert(0,num)
                if i < 0:
                    result.insert(0,1)
            else:
                num += 1
                result.insert(0,num)
                break
        while i >= 0:
            result.insert(0,digits[i])
            i -= 1
        
        return result
            
        
# @lc code=end

