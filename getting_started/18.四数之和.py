# @before-stub-for-debug-begin
from python3problem18 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        
        if n < 4 :
            return []
        
        nums.sort()
        result = []
        
        for i in range(n-3):
            x = nums[i]
            
            if i > 0 and x == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                y = nums[j]
            
                if j > i+1 and y == nums[j-1]:
                    continue
                
                p = j + 1
                q = n - 1
                
                while p<q:
                    a = nums[p]
                    b = nums[q]
                    temp = x+y+a+b
                    if temp == target:
                        result.append([x,y,a,b])
                        p += 1
                        while p < q and nums[p] == nums[p-1]:
                            p += 1
                        q -= 1
                        while q > p and nums[q] ==  nums[q+1]:
                            q -= 1
                    elif temp > target:
                        q -= 1
                        while q > p and nums[q] ==  nums[q+1]:
                            q -= 1
                    else:
                        p += 1
                        while p < q and nums[p] == nums[p-1]:
                            p += 1
        return result
            
        '''
            j = i+1
            k = n-1
            while j<k-1:
                y = nums[j]
                z = nums[k]
                temp = x + y + z
                
                if temp < target:
                    p = k -1 
                    while p > j:
                        a = nums[p]
                        if temp + a == target:
                            result.append([x,y,a,z])
                            break
                        p -= 1
                    # tempj = nums[j]
                    j += 1
                    while nums[j]==nums[j-1] and j < k-1:
                        j += 1
                elif temp > target:
                    p = j + 1 
                    while p < k:
                        a = nums[p]
                        if temp + a == target:
                            result.append([x,y,a,z])
                            break
                        p += 1
                    # tempj = nums[j]
                    k -= 1
                    while k > j+1 and nums[k]==nums[k+1]:
                        k -= 1
                else:
                    p = j + 1 
                    while p < k:
                        a = nums[p]
                        if temp + a == target:
                            result.append([x,y,a,z])
                            break
                        p += 1
                    
                    testj = j + 1
                    while nums[testj]==nums[testj-1] and testj < k-1:
                        testj += 1
                    testk = k-1
                    while testk > j+1 and nums[testk]==nums[testk+1]:
                        testk -= 1
                    if abs(x + nums[testj] +z -target)>abs(x + y + nums[testk]-target):
                        k = testk
                    else:
                        j = testj
        
            
        return result
        '''
                
# @lc code=end

