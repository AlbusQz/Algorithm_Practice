#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = copy.deepcopy(nums)
        self.n = len(nums)


    def reset(self) -> List[int]:
        return self.nums


    def shuffle(self) -> List[int]:
        nums = copy.deepcopy(self.nums)
        for i in range(self.n):
            j = random.randrange(i,self.n)
            nums[i],nums[j] = nums[j], nums[i]
        return nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

