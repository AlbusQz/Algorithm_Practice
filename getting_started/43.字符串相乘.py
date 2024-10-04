# @before-stub-for-debug-begin
from python3problem43 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
                
        if num1 == '0' or num2 == '0':
            return '0'

        char2int = {
            '0' : 0 ,
            '1' : 1 ,
            '2' : 2 ,
            '3' : 3 ,
            '4' : 4 ,
            '5' : 5 ,
            '6' : 6 ,
            '7' : 7 ,
            '8' : 8 ,
            '9' : 9 ,
        }
        
        def add_two_list(list1,list2,n = 400,m = 400):
            # print(list1)
            # print(list2)
            l = max(n,m)+1
            mid = [0 for _ in range(l)]
            i = 0
            while i<n and i<m:
                temp = list1[n-i-1] + list2[m-i-1] + mid[l-i-1]
                if temp >= 10:
                    temp = temp % 10
                    mid[l-i-2] += 1
                mid[l-i-1] = temp
                i += 1
            if i < n :
                while i < n:
                    temp = list1[n-i-1] + mid[l-i-1]
                    if temp >= 10:
                        temp = temp % 10
                        mid[l-i-2] += 1
                    mid[l-i-1] = temp
                    i += 1
            else:
                while i < n:
                    temp = list2[m-i-1] + mid[l-i-1]
                    if temp >= 10:
                        temp = temp % 10
                        mid[l-i-2] += 1
                    mid[l-i-1] = temp
                    i += 1
            # print(mid)
            if mid[0] == 0:
            #     l += 1
            # else:
                mid = mid[1:]
                l -= 1
            return mid,l
        
        def mul_list_num(list1,num,n,j):
            
            mid_1 = [0 for _ in range(n)]
            mid_2 = [0 for _ in range(n)]
            for i in range(n):
                temp = char2int[num]*char2int[list1[n-i-1]]
                mid_2[n-i-1] = temp % 10
                # print(int(temp/10))
                # print(n-i-1)
                mid_1[n-i-1] = int(temp/10)
            # print(mid_1) 
            # print(mid_2)
            
            for i in range(j):
                mid_1.append(0)
                mid_2.append(0)
            mid_1.append(0)
            
            if mid_1[0] == 0:
                mid_1 = mid_1[1:]
                return add_two_list(mid_1,mid_2,n+j,n+j)
            else:
                return add_two_list(mid_1,mid_2,n+j+1,n+j)
        
        n = len(num1)
        m = len(num2)
        # l = n+m+1
        l = 1
        result = [0]
        for i in range(n):
            temp_r, temp_l = mul_list_num(num2,num1[n-i-1],m,i)
            # print(temp_r)
            
            result , l = add_two_list(temp_r,result,temp_l,l)
            # print(result)
        
        s = ""
        for i in range(l):
            s += str(result[i])
        
        return s
        
# s1 = '123'
# s2 = '456'
# s = Solution()
# print(s.multiply(s1,s2))  
        
# @lc code=end

