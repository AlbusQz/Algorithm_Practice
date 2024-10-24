#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # root = '/'
        queue = []
        index = 0
        paths = path.split('/')

        n = len(paths)

        for i in range(n):
            if paths[i] == '.' or paths[i] == '':
                continue
            if paths[i] == '..':
                if index >0:
                    queue.pop(index-1)
                    index -= 1
            else:
                queue.append(paths[i])
                index += 1
        result = '/'
        for i in range(index):
            result += queue[i]
            if i < index-1:
                result += '/'
            
        return result
# @lc code=end

