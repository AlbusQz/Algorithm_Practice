#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ## 排列组合法
        top = m + n - 2
        bottom = 1
        result = 1
        for i in range(min(m,n)-1):
            result *= top
            result /= bottom
            top -= 1 
            bottom +=1
        return int(result)
# @lc code=end

