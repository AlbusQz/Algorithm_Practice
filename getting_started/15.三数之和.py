# @before-stub-for-debug-begin
from python3problem15 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ##with leetcode's help(double pointer)
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                k = n - 1
                for j in range(i+1,n-1):
                    if (j!= i+1 and nums[j] == nums[j-1]) or nums[i] + nums[j] + nums[k] < 0:
                        # j += 1
                        continue
                    while j<k and nums[i] + nums[j] + nums[k] >0 :
                        k -= 1
                    if not(j<k):
                        break
                    elif nums[i] + nums[j] + nums[k] == 0 :
                        result.append([nums[i],nums[j],nums[k]])
                        continue
                '''
                j = i+1
                k = n-1
                while j<k:
                    if (j!= i+1 and nums[j] == nums[j-1]) or nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                        continue
                    elif (k!= n-1 and nums[k] == nums[k+1]) or nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                        continue
                    else:
                        result.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1  '''
        return result
                
        
        ## brute force
        '''
        hashtable = set()
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            for j in range(i+1,n):
                num2 = nums[j]
                for k in range(j+1,n):
                    num3 = nums[k]
                    if num1+num2+num3==0:
                        l = [num1,num2,num3]
                        l.sort()
                        hashtable.add(tuple(l))
        result = list(hashtable)
        return result
        '''
# @lc code=end
        
