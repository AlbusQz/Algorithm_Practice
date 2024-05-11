class Solution(object):
    def brute_force_twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            # for j in range(len(nums)-i-1):
            for j in range(i+1, len(nums)):
                # if nums[i]+nums[j+i+1] == target:
                if nums[i]+nums[j] == target:
                    # return [i,j+i+1]
                    return [i,j]
                    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # temp_hash = dict()
        # for i,item in enumerate(nums):
        #     if (target - item) in temp_hash:
        #         return [temp_hash[target - item],i]
        #     else:
        #         temp_hash[item] = i
        temp_hash = dict()
        for i,item in enumerate(nums):
            if (item) in temp_hash:
                return [temp_hash[item],i]
            else:
                temp_hash[target - item] = i

if __name__ == '__main__':
    nums = [3,2,4]#[2,7,11,15]
    target = 6
    solution = Solution() 
    print(solution.brute_force_twoSum(nums,target))
    print(solution.twoSum(nums,target))