#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        #递归法dfs
        m = len(board)
        n = len(board[0])
        s = len(word)
        
        visited = [[False for _ in range(n)]for _ in range(m)]
              
        def dfs(x,y,depth):
            # if visited[x][y] == True:
            #     return False
            # visited[x][y] = True
            if board[x][y] != word[depth]:
                return False
            elif depth == s-1:
                return True
            flag0 = False
            flag1 = False
            flag2 = False
            flag3 = False
            if x > 0 and visited[x-1][y] == False:
                visited[x-1][y] = True
                flag0 = dfs(x-1,y,depth+1)
                visited[x-1][y] = False
            if x < m-1 and visited[x+1][y] == False:
                visited[x+1][y] = True
                flag1 = dfs(x+1,y,depth+1)
                visited[x+1][y] = False
            if y > 0 and visited[x][y-1] == False:
                visited[x][y-1] = True
                flag2 = dfs(x,y-1,depth+1)
                visited[x][y-1] = False
            if y < n-1 and visited[x][y+1] == False:
                visited[x][y+1] = True
                flag3 = dfs(x,y+1,depth+1)
                visited[x][y+1] = False
            return flag0|flag1|flag2|flag3
        
        for i in range(m):
            for j in range(n):
                visited[i][j] = True
                temp = dfs(i,j,0)
                visited[i][j] = False
                if temp == True:
                    return True
        return False
        
# @lc code=end

