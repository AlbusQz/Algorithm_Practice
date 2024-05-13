#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        in_letter = dict()
        result = 0
        head = 0
        tail = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i,letter in  enumerate(s):
            if letter in in_letter:
                tail = in_letter[letter]
                for j in range(head,tail):
                    in_letter.pop(s[j])
                in_letter[letter] = i
                head = tail+1
            else:
                in_letter[letter] = i
            if len(in_letter) > result:
                result = len(in_letter)
        return result
# @lc code=end

