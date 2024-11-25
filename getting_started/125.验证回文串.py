#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                s_new += i
        s_new = s_new.lower()
        n = len(s_new)
        i = 0
        j = n-1
        while i <= j:
            if s_new[i] != s_new[j]:
                return False
            i += 1
            j -= 1
        return True
# @lc code=end

