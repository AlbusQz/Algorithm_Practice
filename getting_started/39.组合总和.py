#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        n = len(candidates)
        candidates.sort()
        queue = []
        index = {}
        
        for i in range(n):
            value = candidates[i]
            if value == target:
                result.append([value])
                continue
            queue.append([value])
            index[value] = i
        
        # top = 0
        bottom = n
        
        while bottom>0:
            new_queue = []
            for l in queue:
                
                ##获取取值的开始坐标
                l_max = max(l)
                l_value = sum(l)
                begin_index = index[l_max]
                
                ##队列扩展
                for i in range(begin_index,n):
                    temp_value = candidates[i] + l_value
                    if temp_value == target:
                        l.append(candidates[i])
                        result.append(l)
                        break
                    if temp_value < target:
                        temp_l = copy.copy(l)
                        temp_l.append(candidates[i])
                        new_queue.append(temp_l)
                        continue            
            
            del(queue)
            queue = new_queue
            bottom = len(new_queue)
            
        return result
        
# @lc code=end

