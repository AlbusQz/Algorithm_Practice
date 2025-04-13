#
# @lc app=leetcode.cn id=399 lang=python
#
# [399] 除法求值
#

# @lc code=start
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        ## build matrix
        node_dict = {}
        m = 0
        for e in equations:
            if e[0] not in node_dict:
                node_dict[e[0]] = m
                m += 1
            if e[1] not in node_dict:
                node_dict[e[1]] = m
                m += 1
        
        matrix = [[0 for _ in range(m)]for _ in range(m)]
        
        for i in range(m):
            matrix[i][i] = 1
        
        n = len(equations)
        for i in range(n):
            x = node_dict[equations[i][0]]
            y = node_dict[equations[i][1]]
            v = values[i]
            matrix[x][y] = v
            matrix[y][x] = 1/v
        
        ## answering queries
        result = []
        for q in queries:
            x = q[0]
            y = q[1]
            if x not in node_dict or y not in node_dict:
                result.append(-1.0)
                continue
            x = node_dict[x]
            y = node_dict[y]
            visited = [False for _ in range(m)]
            stack = [x]
            vs = [1]
            flag = False
            while len(stack) > 0:
                node = stack.pop()
                v = vs.pop()
                if node == y:
                    result.append(v)
                    flag = True
                    break
                visited[node] = True
                for i in range(m):
                    if visited[i] or matrix[node][i] == 0:
                        continue
                    stack.append(i)
                    vs.append(v*matrix[node][i])
                    matrix[x][i] = v*matrix[node][i]
            if flag == False:
                result.append(-1)
        
        return result
            
# @lc code=end

