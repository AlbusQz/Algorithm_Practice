#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l_max = 0
        n = len(s)
        result = ''
        
        for i in range(n):
            left = i
            right = i+1
            
            temp_l = 0
            while left >=0 and right <n:
                if s[left] == s[right]:
                    temp_l += 2
                    left -= 1
                    right += 1
                else:
                    break
            if temp_l > l_max:
                l_max = temp_l
                result = s[left+1:right-1+1]
            
            left = i-1
            right = i+1
            
            temp_l = 1
            while left >=0 and right <n:
                if s[left] == s[right]:
                    temp_l += 2
                    left -= 1
                    right += 1
                else:
                    break
            if temp_l > l_max:
                l_max = temp_l
                result = s[left+1:right-1+1]
        
        return result
# @lc code=end

