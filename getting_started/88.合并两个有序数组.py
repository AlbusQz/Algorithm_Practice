#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ## 双指针法
        nums3 = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i]< nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                nums3.append(nums1[i])
                i += 1
        elif j < n:
            while j < n:
                nums3.append(nums2[j])
                j += 1
        for i in range(m+n):
            nums1[i] = nums3[i]
        
# @lc code=end

