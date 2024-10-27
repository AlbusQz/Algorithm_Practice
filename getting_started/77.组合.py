#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []
        combines = [[(i+1)] for i in range(n-k+1)]
        max_index = [(i+1) for i in range(n-k+1)]
        for i in range(k-1):
            temp_combines= []
            temp_max_index = []
            l = len(combines)
            for j in range(l):
                temp = combines[j]
                temp_index = max_index[j]
                for k in range(temp_index+1,n+1):
                    temp_c = copy.copy(temp)
                    temp_c.append(k)
                    temp_combines.append(temp_c)
                    temp_max_index.append(k)
            del(combines)
            del(max_index)
            combines = temp_combines
            max_index = temp_max_index
        return combines
            
        
        
# @lc code=end

