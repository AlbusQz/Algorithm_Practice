#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        ## 纯粹的暴力模拟做法（有有限状态机的做法）
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        purenum_char = '0123456789'

        if n == 1 and s[0] not in purenum_char:
            return False
        
        # 合法字符表
        valid_char = "0123456789eE.+-"
        num_char = '01234567890.'
        

        e_s = 0
        part1_begin = 0
        part1_l = 0
        part2_begin = 0
        part2_l = 0
        points = 0
        e = -1
        pluses = 0
        
        ## 第一次进行扫描
        for i in range(n):
            
            c = s[i]
            ## 判断字符合法
            if c not in valid_char:
                return False
            ## 判断正负号正确
            if c == '+' or c == '-':
                if i != 0:
                    if s[i-1] != 'e' and s[i-1] !='E':
                        return False
                
                part1_begin += 1
            
            if c == '.':
                points += 1
                if points >1:
                    return False

            if c == 'E' or c == 'e':
                e_s += 1
                if e_s >1:
                    return False
                if i == 0:
                    return False
                if s[i-1] not in num_char:
                    return False
                if i == n-1:
                    return False
                e = i
        if e < 0:
            part1_l = n - part1_begin
        else:
            part1_l = e - part1_begin
            if s[e+1] != '+' and s[e+1] != '-':
                part2_begin = e+1
            else:
                part2_begin = e+2
            part2_l = n - part2_begin
        

        #检查part1
        if part1_l == 1 and s[part1_begin] == '.':
            return False
        points = 0
        for i in range(part1_l):
            c = s[part1_begin+i]
            if c not in num_char:
                return False
            if c == '.':
                points +=1
                if points>1:
                    return False
        #检查part2
        if part2_begin != 0 and part2_l == 0:
            return False
        points = 0
        for i in range(part2_l):
            c = s[part2_begin+i]
            if c not in num_char:
                return False
            if c == '.':
                return False

        return True

        
        
# @lc code=end

