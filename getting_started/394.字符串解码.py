#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def decodeKstr(i,k,s):
            index = i + 2
            result = ""
            n = len(s)
            while index < n:
                c = s[index]
                if c.isdigit() == True:
                    temp_index = index + 1
                    while s[temp_index] != '[':
                        temp_index += 1
                    temp_k = int(s[index:temp_index])
                    j,temp_result = decodeKstr(temp_index-1,temp_k,s)
                    index = j + 1
                    result += temp_result
                    continue
                if c == ']':
                    temp_result = ''
                    for _ in range(k):
                        temp_result += result
                    break
                result += s[index]
                index += 1
            return index,temp_result

        return decodeKstr(-2,1,s+']')[1]
                

# @lc code=end

