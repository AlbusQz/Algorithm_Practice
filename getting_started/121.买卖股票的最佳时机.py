#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        result = 0
        temp_max = -1
        maxes = []
        for i in range(n-1,-1,-1):
            if prices[i] > temp_max:
                temp_max = prices[i]
            maxes.insert(0,temp_max)
        
        for i in range(n):
           temp = maxes[i] - prices[i]
           result = max(temp,result)
        return result
        # @lc code=end

