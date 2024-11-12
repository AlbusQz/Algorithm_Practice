#
# @lc app=leetcode.cn id=97 lang=python
#
# [97] 交错字符串
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        ## dp法（即是否相同只与两个字符串的当前状态和前一个字符有关）
        
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        
        dp = [[False for _ in range(n+1)]for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(m+1):
            for j in range(n+1):
                p = i + j - 1
                if i > 0:
                    if dp[i-1][j] and s1[i-1] == s3[p]:
                        dp[i][j] = True
                        continue
                if j > 0:
                    if dp[i][j-1] and s2[j-1] == s3[p]:
                        dp[i][j] = True
                        continue
        
        return dp[m][n]
                
        
        
        
        ## 搜索法，会超时
        '''
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m + n:
            return False
        if l == 0:
            return True
        if m == 0:
            return s2 == s3 
        if n == 0:
            return s1 == s3 
        i = 0
        ps = [0]
        qs = [0]
        
        while i < l:
            
            temp_ps = []
            temp_qs = []
            
            k = len(ps)
            if k == 0:
                return False
            
            for j in range(k):
                # print(j)
                # print(ps)
                # print("_____")
                p = ps[j]
                q = qs[j]
                if p < m and s3[i] == s1[p]:
                    temp_ps.append(p + 1)
                    temp_qs.append(q)
                if q < n and s3[i] == s2[q]:
                    temp_ps.append(p)
                    temp_qs.append(q + 1)
            del ps
            del qs
            ps = temp_ps
            qs = temp_qs   
            
            i += 1
            
        return True
        '''
# @lc code=end

