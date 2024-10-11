#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ## 暴力法，应该会超时
        n = 0
        result = []
        ## 乘二的目的是为了区分连续，即偶数下标为start/end，奇数用于区分两个点之间是否连续
        board = [False for _ in range(20002)]
        for i in intervals:
            n = max(i[1],n)
            if i[0] == i[1]:
                board[i[0]*2] = True 
            for j in range(i[0]*2,i[1]*2):
                board[j] = True
        
        left = 0
        right = 0
        n = 2 * n
        print(board[:n])
        while left <= n and right <= n:
            if board[left] == True:
                right = left + 1
                while board[right] == True and right <n:
                    right += 1
                result.append([left/2,int(right/2)])
                left = right + 1 
            else:
                if left % 2 ==1:
                    left += 1
                else:
                    left += 2
        return result
            
        
        
# @lc code=end

