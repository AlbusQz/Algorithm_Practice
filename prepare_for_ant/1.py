def findMissingNum(nums):
    n = len(nums)
    result = []
    visited = [False for _ in range(n)]
    for i in nums:
        visited[i-1] = True
    for i in range(n):
        if visited[i] == False:
            result.append(i+1)
    return result

if __name__ == "__main__":
    input0 = [2, 1, 2, 2, 2, 2, 3, 5, 7, 8]
    output0 = findMissingNum(input0)
    print(output0)
    input1 = [1,2,3,4,5]
    output1 = findMissingNum(input1)
    print(output1)
    input2 = [2,2,2,2,2]
    output2 = findMissingNum(input2)
    print(output2)
    