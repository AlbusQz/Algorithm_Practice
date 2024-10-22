#评测题目2: 解析IP地址
# "127.0.0.1" -> int32_t
#2130706433

def string2int_IP(s):
    
    nums = s.split('.')
    n = len(nums)
    result = 0
    for i in range(n):
        c = nums[i]
        if c.isdigit() == False:
            print('Error,not a IP address!')
            return -1
        else:
            temp = int(c)
            if temp < 0 or temp > 255:
                print('Error,not a IP address!')
                return -1
            result += temp
            if i != n-1:
                result = result << 8
    return result

if __name__ == '__main__':
    input0 = "127.0.0.1"
    output0 = string2int_IP(input0)
    if output0>0:
        print(output0)
        
    input1 = "127.0.199.1"
    output1 = string2int_IP(input1)
    if output1>0:
        print(output1)
        
    input2 = "127.0.259.1"
    output2 = string2int_IP(input2)
    if output2>0:
        print(output2)
        
    input3 = "127.0.0.-1"
    output3 = string2int_IP(input3)
    if output3>0:
        print(output3)
        
    input4 = "127.a.0.1"
    output4 = string2int_IP(input4)
    if output4>0:
        print(output4)