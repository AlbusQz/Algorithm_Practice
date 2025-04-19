#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        m = len(s)
        n = len(p)
        if m < n:
            return []
        chars_dict = {}
        count_dict = {}
        index = 0
        for i in p:
            if i in chars_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
                chars_dict[i] = index
                index += 1
        

        c = len(chars_dict)
        chars = [0 for _ in range(c)]
        
        for i in chars_dict:
            chars[chars_dict[i]] = count_dict[i]

        temp_chars = copy.copy(chars)
        result = []
        i = 0
        temp = ''
        while i < m:
            temp_c = s[i]
            # print(temp_chars)
            if len(temp) == n:
                if sum(temp_chars) == 0:
                    result.append(i-n)
                
                if temp_c not in chars_dict:
                    i += 1
                    temp_chars = copy.copy(chars)
                    temp = ''
                    continue
                                
                remove_c = s[i-n]
                temp_chars[chars_dict[remove_c]] += 1
                temp = temp[1:]
                
                if temp_chars[chars_dict[temp_c]] > 0:
                    temp_chars[chars_dict[temp_c]] -= 1
                    temp += temp_c
                    i += 1
                    continue
                else:
                    
                    for j in temp:
                        temp_chars[chars_dict[j]] += 1
                        temp = temp[1:]
                        if j == temp_c:
                            break
                        
                    temp_chars[chars_dict[temp_c]] -= 1
                    temp += temp_c
                    i += 1
                    continue
                
            elif len(temp) < n:
                if temp_c not in chars_dict:
                    i += 1
                    temp = ''
                    temp_chars = copy.copy(chars)
                    continue
                if temp_chars[chars_dict[temp_c]] > 0:
                    temp_chars[chars_dict[temp_c]] -= 1
                    temp += temp_c
                    i += 1
                    continue
                else:
                    for j in temp:
                        temp_chars[chars_dict[j]] += 1
                        temp = temp[1:]
                        if j == temp_c:
                            break
                        
                    temp_chars[chars_dict[temp_c]] -= 1
                    temp += temp_c
                    i += 1
                    continue
        if sum(temp_chars) == 0:
            result.append(m-n)
        return result
                
        
        
        
# @lc code=end

