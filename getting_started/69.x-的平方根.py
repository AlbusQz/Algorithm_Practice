#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x

        left = 1
        right = x
        while right > left +1 :
            mid = int((left + right)/2)

            temp = mid **2
            if temp < x :
                left = mid
            elif temp == x:
                return mid
            else:
                right = mid
        
        return int((left + right)/2)
        
# @lc code=end

