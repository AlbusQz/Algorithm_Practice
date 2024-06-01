#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        min_len = len(strs[0])
        n = len(strs)
        
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                
        for i in range(min_len):
            t = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != t:
                    return result
            result += t
        return result
# @lc code=end

