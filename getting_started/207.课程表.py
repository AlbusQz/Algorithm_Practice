#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        if n == 0 or numCourses == 1:
            return True
        in_times = [0 for _ in range(numCourses)]
        next = [[] for _ in range(numCourses)]
        for i in prerequisites:
            in_times[i[1]] += 1
            next[i[0]].append(i[1])
        oks = 0
        queue = []
        for i in range(numCourses):
            if in_times[i] == 0:
                queue.append(i)
                oks += 1
        while len(queue) > 0:
            head = queue.pop(0)
            for i in next[head]:
                in_times[i] -= 1
                if in_times[i] == 0:
                    queue.append(i)
                    oks += 1
        if oks == numCourses :
            return True
        else:
            return False
# @lc code=end

