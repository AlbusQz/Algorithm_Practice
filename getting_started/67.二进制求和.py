#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        n = len(a)
        m = len(b)
        
        up = 0
        
        i = 0
        j = 0
        
        result = ''
        while n-1-i >= 0 and m-1-j >=0 :
            # temp_count = up
            if a[n-1-i] == '1':
                up += 1
            if b[m-1-j] == '1':
                up += 1
            if up == 0:
                result = '0' + result
            elif up == 1:
                result = '1' + result
                up = 0
            elif up == 2:
                result = '0' + result
                up = 1
            else:
                result = '1' + result
                up = 1
                
            i += 1
            j += 1
        
        while n-1-i >= 0:
            if a[n-1-i] == '1':
                up += 1
            if up == 0:
                result = '0' + result
            elif up == 1:
                result = '1' + result
                up = 0
            else:
                result = '0' + result
                up = 1
                
            i += 1
            
        while m-1-j >=0 :
            
            if b[m-1-j] == '1':
                up += 1
            if up == 0:
                result = '0' + result
            elif up == 1:
                result = '1' + result
                up = 0
            else:
                result = '0' + result
                up = 1

            j += 1
        if up > 0:
            result = '1' + result
        
        return result
        
        
# @lc code=end

