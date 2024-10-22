# //评测题目4: 
# //输入：给定一个无重复元素的整数数组numbers和一个目标整数target。
# //输出：找出numbers中可以使数字和为目标数target的所有不同组合，并以列表形式返回。
# //e.g., 输入: nums = [2,3,5], target = 8
# //输出: [[2,2,2,2],[2,3,3],[3,5]]
import copy

def findSum(nums,target):
    if max(nums)<0 and target >= 0:
        return []
    if min(nums)>0 and target <= 0:
        return []
    if max(nums) <= 0 and target >0:
        return []
    if min(nums)>=0 and target < 0:
        return []
    nums.sort()
    n = len(nums)
    queue = []
    index = {}
    result = []
    for i in range(n):
        value = nums[i]
        if value == target:
            result.append([value])
            continue
        queue.append([value])
        index[value] = i
    
    bottom = n
    while bottom>0:
        new_queue = []
        for l in queue:

            l_max = max(l)
            l_value = sum(l)
            begin_index = index[l_max]

            for i in range(begin_index,n):
                temp_value = nums[i] + l_value
                if temp_value == target:
                    l.append(nums[i])
                    result.append(l)
                    break
                if temp_value < target:
                    temp_l = copy.copy(l)
                    temp_l.append(nums[i])
                    new_queue.append(temp_l)
                    continue            
        
        del(queue)
        queue = new_queue
        bottom = len(new_queue)
    return result
    
if __name__ == "__main__" :
    nums0 = [2,3,5]
    target0 = 8
    print(findSum(nums0,target0))
    
    nums1 = [2,3,5,6,8]
    target1 = 8
    print(findSum(nums1,target1))
    
    nums2 = [2,3,5,6,8]
    target2 = 8
    print(findSum(nums2,target2))
    
    nums3 = [2,3,5]
    target3 = 0
    print(findSum(nums3,target3))
    
    nums4 = [-2,0,-5]
    target4 = 10
    print(findSum(nums4,target4))
    
    nums5 = [2,4,6]
    target5 = 13
    print(findSum(nums5,target5))