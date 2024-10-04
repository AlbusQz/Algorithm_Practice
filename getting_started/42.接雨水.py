#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int: 
        
        ## 单调栈匹配法，通过类似括号匹配的思路进行解决
        stack = []
        n = len(height)
        
        stack.append(height[0])
        l = 0
        r = 0
        top = 0
        
        for i in range(n):
            
        
        ## 双指针法,优化掉了原来需要的存储空间
        '''
        result = 0
        n = len(height)
        left = 0
        right = n-1
        leftmax = height[0]
        rightmax = height[-1]
        
        while left < right:
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])
            
            if leftmax < rightmax:
                
                result += leftmax - height[left]
                left += 1
                
            else:
                
                result += rightmax - height[right]
                right -= 1
        return result
        '''
        
        
        
        ## DP法
        '''
        n = len(height)
        left = []
        right = []
        # left.append(height[0])

        before = 0
        for i in range(n):
            if height[i] > before:
                before = height[i]
            left.append(before)
        
        before = 0
        for i in range(n-1,-1,-1):
            if height[i]>before:
                before = height[i]
            right.insert(0,before)
        
        result = []
        for i in range(0,n):
            result.append(min(left[i],right[i])-height[i])
        result = sum(result)
        return result
        '''
        

        
# @lc code=end

        ## 暴力法，会超时
        '''
        n = len(height)
        
        def count_v(h):
            result = 0
            flags = []
            begin = 0
            b_flag = False
            for i in range(n):
                if height[i] < h :
                    flags.append(True)
                    if b_flag == False:
                        begin = i+1
                else:
                    flags.append(False)
                    b_flag = True
                    end = i+1
            # begin = 0
            # end = n
            # print(begin)
            # while flags[begin] == True and begin < end:
            #     begin += 1
            # while flags[end-1] == True and end > begin:
            #     end -= 1

            for i in range(begin,end):
                if flags[i] == True:
                    result += 1
            return result
                    
            
        
        result = 0
        
        
        height_max = max(height)
        
        for i in range(height_max):
            result += count_v(i+1)
            # print(count_v(i+1))
        
        return result
        '''