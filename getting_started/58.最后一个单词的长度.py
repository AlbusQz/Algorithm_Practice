#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        n = len(s)
        i = n-1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        while i >=0 and s[i] != ' ':
            i -= 1
            l += 1
        return l
        
# @lc code=end

