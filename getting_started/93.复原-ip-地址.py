#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []
        
        n = len(s)
        if n < 4 or n > 12:
            return result

        def isvalid(temp_s):
            if len(temp_s) > 1 and temp_s[0] == '0':
                return False
            temp_i = int(temp_s)
            if temp_i < 0 or temp_i > 255:
                return False
            return True
        
        def list2str(ip_list):
            result = ''
            for i in ip_list:
                result += i
                result += '.'
            # result -= '.'
            return result[:-1]
                
        stack = []
        lens = []
        
        for i in range(1,4):
            if isvalid(s[:i]):
                stack.append([copy.copy(s[:i])])
                lens.append(i)
        
        while len(stack) > 0:
            
            top = stack.pop()
            l = lens.pop()
            m = len(top)
            if m == 4 and l == n:
                result.append(list2str(top))
                print(l)
                continue
            if l == n:
                continue
            for i in range(1,4):
                if l + i > n:
                    continue
                if isvalid(s[l:l+i]):
                    top.append(s[l:l+i])
                    l += i
                    stack.append(copy.copy(top))
                    lens.append(l)
                    top.pop()
                    l -= i
                    
        return result
            
            

# @lc code=end

