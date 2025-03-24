#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## brute force
        '''
        dic = {}
        n = len(nums)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            if dic[i] > int(n/2):
                    return i
        return -1
        '''
        ## Boyer-Moore 投票算法，实在是太妙了
        can = nums[0]
        count = 1
        n = len(nums)
        for i in range(1,n):
            if count == 0:
                can = nums[i]
            if can == nums[i]:
                count += 1
            else:
                count -= 1
        return can
# @lc code=end

