#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []
        queue = []
        cs = []
                
        ## 数据准备
        n = len(candidates)
        candidates.sort()
        index = {}
        count = {}
        before = 0
        now_count = 0
        for i in range(n):
            now = candidates[i]
            if now != before:
                # index[now] = i
                queue.append([now])
                cs.append(now)
                if now_count >0 :
                    count[before] = now_count
                now_count = 1
            else:
                now_count += 1

            before = now
        
        count[before] = now_count
        counts = []
        m = len(queue)
        m_c = len(cs)
        for i in range(m_c):
            temp_count = copy.copy(count)
            temp_count[cs[i]] -= 1
            index[cs[i]] = i
            counts.append(temp_count)
        ##进行筛选
        while m>0:
            temp_queue = []
            temp_counts = []
            for i in range(m):
                # print(queue)
                now_count = counts[i]
                now_c = queue[i]
                now_max = max(now_c)
                now_index = index[now_max]
                # print(now_index)
                now_value = sum(now_c)
                
                if now_value == target:
                    result.append(now_c)
                    continue
                if now_value > target:
                    continue

                for j in range(now_index,m_c):
                    temp_count = copy.copy(now_count)
                    v = cs[j]

                    if temp_count[v]>0 and now_value + v <= target:
                        
                        c = copy.copy(now_c)
                        c.append(v)
                        temp_queue.append(c)
                        temp_count[v] = temp_count[v] -1
                        temp_counts.append(temp_count)

            del(queue)
            del(counts)
            queue = temp_queue
            counts = temp_counts
            m = len(queue)      # print(count)
             
        
        return result
        
# @lc code=end

