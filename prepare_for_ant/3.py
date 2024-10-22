# //评测题目3: 
# // abab, xyxy => true
# // abc, xyz => true
# // abba, aaaa => false
# // abba, baab => true
# // abc, bcd => true
# // abc, xxx => false

def patternSame(s0,s1):
    
    m = len(s0)
    n = len(s1)
    if m != n:
        return False
    pattern = {}
    for i in range(m):
        c0 = s0[i]
        c1 = s1[i]
        if c0 in pattern:
            if pattern[c0] != c1:
                return False
        else:
            pattern[c0] = c1
    pattern = {}
    for i in range(m):
        c0 = s0[i]
        c1 = s1[i]
        if c1 in pattern:
            if pattern[c1] != c0:
                return False
        else:
            pattern[c1] = c0
    return True

if __name__ == '__main__':
    
    c0 = 'abab'
    c1 = 'xyxy'
    print(patternSame(c0,c1))
    
    c2 = 'abc'
    c3 = 'xyz'
    print(patternSame(c2,c3))
    
    c4 = 'abba'
    c5 = 'aaaa'
    print(patternSame(c4,c5))
    
    c6 = 'abba'
    c7 = 'baab'
    print(patternSame(c6,c7))
    
    c8 = 'abc'
    c9 = 'bcd'
    print(patternSame(c8,c9))
    
    c10 = 'abc'
    c11 = 'xxx'
    print(patternSame(c10,c11))
    
    c12 = 'aa'
    c13 = 'xxx'
    print(patternSame(c12,c13))
    