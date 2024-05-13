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

    #官方方法:滑动窗口，确实比我的更加精妙好理解（但效率好像不如我的？）
    '''
    def lengthOfLongestSubstring(self, s):
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
    '''
# @lc code=end

