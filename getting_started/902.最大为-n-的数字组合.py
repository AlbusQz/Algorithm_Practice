#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#

# @lc code=start
class Solution:
    ## 主题思想：
    '''
        原本直接用dfs搜索会超时。
        
        选择使用分治的方式：
            当使用的数字数量小于数字位数时候，
            直接用排列的方式得出答案；
            当使用的数字数量等于数字位数时候，
            用搜索的方式，计算可行的数字个数；
        最后相加得出结果
    '''
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        m = n
        t = 0
        d = []
        temps = []
        ms = []
        while m >0:
            t += 1
            ms.insert(0,m%10)
            m = int(m/10)

        result = 0
        len_d = len(digits)
        temp = 1
        temps.insert(0,temp)
        for i in range(1,t):
            temp *= len_d
            result += temp
            temps.insert(0,temp)
            
        def get_temp(index):
            if index == t-1:
                temp = 0
                for j in digits:
                    if int(j) <= ms[index]:
                        temp += 1
                    else:
                        break
                return temp
            temp = 0
            for j in digits:
                if int(j) < ms[index]:
                    temp += temps[index]
                elif int(j) == ms[index]:
                    temp += get_temp(index +1)
                else:
                    break
            return temp
        result += get_temp(0)
        return result       
# @lc code=end

