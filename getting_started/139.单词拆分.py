#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ## 首先试图使用递归的方法[个人感觉有点慢的]
        left_stack = []
        right_stack = []
        stack = []
        left = 0
        right = 0
        i = 0
        m = len(s)
        n = len(wordDict)
        def findsubstring(i):
            if i == m:
                return True
            result = False
            for j in range(i,m):
                if s[i:j+1] in wordDict:
                    # print(s[i:j+1])
                    # stack.append(s[i:j+1])
                    # print((j))
                    result = result or findsubstring(j+1)
            # if len(stack)  != 0:
            #     stack.pop()
            return result
        
        result = findsubstring(0)
        return result
                
# @lc code=end

