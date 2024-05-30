# @before-stub-for-debug-begin
from python3problem11 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    
    #使用了DP的方法，引入了很多的重复运算导致超时（O(n)=n^2）
    def maxArea_dp(self, height: List[int]) -> int:
        n = len(height)
        v = [[0 for i in range(n)]for j in range(n)]
        result = 0
        
        for i in range(n-1):
            for j in range(i+1,n):
                v[i][j] = max(v[i][j-1],(j-i)*min(height[i],height[j]))
            if v[i][j]>result:
                result = v[i][j]
                
        return result
    
    #应当使用双指针的方法解决
    #原理：指针置于两端，每次移动其中的较短的一边，这样使得每次都有可能获得更优的结果（若移动更短边，则不可能会多）
    #leetcode评论解释：感觉这个移动有点博弈论的味了，每次都移动自己最差的一边，虽然可能变得更差，但是总比不动（或者减小）强，动最差的部分可能找到更好的结果，但是动另一边总会更差或者不变，兄弟们，这不是题，这是人生，逃离舒适圈！！（这解释我觉得无敌了，哈哈哈）
    # （O(n)=n^2）
    
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        result = 0
        while i<j:
            if height[i]>height[j]:
                result = max(((j-i)*height[j]),result)
                j = j - 1
            else:
                result = max(((j-i)*height[i]),result)
                i = i + 1
        return result
                
        
# @lc code=end

