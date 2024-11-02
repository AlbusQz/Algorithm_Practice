#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        if n == 0:
            return [0]
        result = [0 for _ in range(n)]
        nums = [temperatures[0]]
        index = [0]
        
        for i in range(1,n):
            temp = temperatures[i]
            if len(nums) == 0 or nums[-1] >= temp:
                nums.append(temp)
                index.append(i)
                continue
            else:

                while len(nums) > 0 and nums[-1] < temp:

                    nums.pop()
                    temp_i = index.pop()
                    result[temp_i] = i - temp_i
                nums.append(temp)
                index.append(i)

        return result
                
        
        
# @lc code=end

