#
# @lc app=leetcode.cn id=57 lang=python
#
# [57] 插入区间
#

# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        begin = -1
        end = -1
        
        n = len(intervals)
        if n == 0:
            return [newInterval]
        a = newInterval[0]
        b = newInterval[1]
        a_flag = False
        b_flag = False
        for i in range(n):
            temp_a = intervals[i][0]
            temp_b = intervals[i][1]
            if (begin <0 or begin % 1 == 0.5) and a_flag == False:
                if a < temp_a:
                    begin = i - 0.5
                    a_flag = True
                elif a > temp_b:
                    begin = i + 0.5
                else:
                    begin = i
            
            if (end<0 or end % 1 == 0.5) and b_flag == False:
                if b < temp_a:
                    end = i - 0.5
                    b_flag = True
                elif b > temp_b:
                    end = i + 0.5
                else:
                    end = i
        
        print(begin)
        print(end)
        
        if begin == end:
            if begin%1 == 0.5:
                intervals.insert(int(begin+0.5),newInterval)
                # return intervals
                
            # else:
            #     return intervals
        else:
            new_i = []
            if begin % 1 == 0.5:
                new_i.append(a)
                begin += 0.5
            else:
                new_i.append(intervals[begin][0])
            
            if end % 1 == 0.5:
                new_i.append(b)
                end -= 0.5
            else:
                new_i.append(intervals[end][1])
            
            for i in range(int(end-begin+1)):
                intervals.pop(int(begin))
            intervals.insert(int(begin),new_i)
        
        return intervals
        
        
            
        
# @lc code=end

