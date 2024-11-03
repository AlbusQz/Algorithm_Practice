#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        if n == 1:
            return heights[0]
        heights.append(0)
        heights = [0]+ heights
        area = 0
        stack = [0]
        index = [0]
        left = 0
        right = 0
        for i in range(1,n+2):
            temp = heights[i]
            # if temp == 0:
            #     continue
            right = i
            if len(stack) ==0 or stack[-1] <= temp:
                left = i
                index.append(i)
                stack.append(temp) 
                continue
            while len(stack) > 0 and stack[-1] > temp:

                temp_area = (right - left) * stack[-1]
                area = max(area,temp_area)
                stack.pop()
                index.pop()
                if len(index) > 0:
                    left = index[-1]
            index.append(i)
            stack.append(temp)
            # left = i 
        
        print(stack)
        print(index)
        # if len(stack) > 0:
        #     i = 0
        #     while i < len(stack) and stack[i] == 0:
        #         stack.pop(0)
        #         index.pop(0)
        #     if len(stack) == 0:
        #         return area
        #     temp_area = min(stack) * (index[-1]-index[0]+1)
        #     area = max(area,temp_area)
            
        return area
                
        
        
# @lc code=end

