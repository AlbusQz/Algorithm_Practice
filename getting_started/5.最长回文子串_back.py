#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    #中心扩展算法
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        length = -1
        n = len(s)
        if n == 1:
            return s
        loc = 0
        for i,t in enumerate(s):
            left = i
            right = i
            while left>=0 and right <= n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left -2 >length:
                # left += 1
                # right -= 1
                length = right - left -2
                loc = left + 1
            left = i
            right = i+1 
            while left>=0 and right <= n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left -2>length:
                # left += 1
                # right -= 1
                length = right - left -2 
                loc = left + 1
                
            #brute force
            #尝试通过引入0.5这么个点来解决‘cbbd’这种情况，但其实上面的这种方法更加优雅
            # p = 0.5 + i
            # for j in range(min(i,n-i)):
            #     if s[i-j]==s[i+j]:
            #         if j>length:
            #             length = j
            #             loc = i
            #     else:
            #         break
            # for j in range(min(int(p),int(n-p))):
            #     q = (2*j +1) * 0.5
            #     if s[int(p-q)]==s[int(p+q)]:
            #         if int(q+0.5)>length:
            #             length = q
            #             loc = p
            #     else:
            #         break
        return s[loc:loc+length+1]
                
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = 'cbbd'
    print(solution.longestPalindrome(s))
    

