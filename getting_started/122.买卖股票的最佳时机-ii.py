#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
        return result
        
# @lc code=end

