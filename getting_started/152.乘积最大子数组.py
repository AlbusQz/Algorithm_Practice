#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## 暴力记录乘积法
        n = len(nums)
        i = 0
        new_nums = []
        
        while i < n:
            num = nums[i]
            if abs(num) != 1 and num != 0:
                new_nums.append(num)
                i += 1
            elif num == 0:
                j = i
                while j < n and abs(nums[j]) == 0:
                    j += 1
                new_nums.append(0)
                i = j
            else:
                j = i
                one = 0
                ne_one = 0
                while j<n and abs(nums[j]) == 1:
                    if nums[j] > 0:
                        one += 1
                    else:
                        ne_one += 1
                    j += 1
                if one > 0:
                    new_nums.append(1)
                if ne_one > 0:
                    if ne_one %2 == 1:
                        new_nums.append(-1)
                    else:
                        new_nums.append(-1)
                        new_nums.append(-1)
                i = j
        
        nums = new_nums
        n = len(nums)
        Max = max(nums)
        products = [[-0.5 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            products[i][i] = nums[i]
            
        
        for i in range(n-1):
            for j in range(i+1,n):
                products[i][j] = products[i][j-1] * nums[j]
                Max = max(Max,products[i][j])

        return Max
            
        
# @lc code=end

