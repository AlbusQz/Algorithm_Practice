#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        n = len(strs)
        i = 0
        result = []
        str_set = {}
        for s in strs:
            temp_l = list(s)
            temp_l.sort()
            temp_s = "".join(temp_l)
            if temp_s in str_set:
                result[str_set[temp_s]].append(s)
            else:
                result.append([s])
                str_set[temp_s] = i
                i += 1
        return result        
        
# @lc code=end

