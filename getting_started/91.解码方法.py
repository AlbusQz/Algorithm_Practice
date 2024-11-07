#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1,n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and s[i-2] != '0' and int(s[i-2:i])<= 26 and int(s[i-2:i]) > 0:
                dp[i] += dp[i-2]
        # print(dp)
        return dp[n] 
# @lc code=end

