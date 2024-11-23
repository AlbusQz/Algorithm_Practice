#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 看了题解后豁然开朗（
        
        n = len(prices)
        if n == 1:
            return 0
        buy1 = [0 for _ in range(n)]
        sell1 = copy.copy(buy1)
        buy2 = copy.copy(buy1)
        sell2 = copy.copy(buy1)
        buy1[0] = -prices[0]
        sell1[0] = 0
        buy2[0] = -prices[0]
        sell2[0] = 0
        for i in range(1,n):
            buy1[i] = max(buy1[i-1],-prices[i])
            sell1[i] = max(sell1[i-1],prices[i] + buy1[i])
            buy2[i] = max(buy2[i-1],sell1[i] - prices[i])
            sell2[i] = max(sell2[i-1],buy2[i] + prices[i])
        return sell2[-1]
# @lc code=end

