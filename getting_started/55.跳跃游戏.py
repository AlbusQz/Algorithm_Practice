#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #尝试了下dp，会超时
        '''
        n = len(nums)
        if n == 1:
            return True
        reach_end = [n-1]
        while len(reach_end) > 0:
            temp = []
            for i in reach_end:
                for j in range(0,i):
                    if nums[j] + j >= i:
                        if j == 0:
                            return True
                        temp.append(j)
            reach_end = temp
        return False
        '''
        
        # 看了solution后，发现简单的贪心就能解决问题
        #k代表的是能到达的最远的地方。因为题目中描述了可以连挑好几步，所以这部分是连续的
        k = 0
        n = len(nums)
        for i in range(n):
            ## 说明已经有地方是到不了的了
            if i > k:
                return False
            
            k = max(k,i+nums[i])
            if k == n:
                return True
        return True
        
        
# @lc code=end

