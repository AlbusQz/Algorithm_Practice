#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        result = 0.0
        n = len(nums1)
        m = len(nums2)
        if (n+m)%2 == 1:
            mid = int((n+m-1)/2)
            if n==0:
                result = nums2[mid]
            elif m == 0:
                result = nums1[mid]
            else:
                end1 = False
                end2 = False
                for k in range(mid+1):
                    if end1:
                        result = nums2[j]
                        j += 1
                    elif end2:
                        result = nums1[i]
                        i += 1
                    else:
                        if nums1[i]<nums2[j]:
                            result = nums1[i]
                            i += 1
                            if(i==n):
                                end1 = True
                        else:
                            result = nums2[j]
                            j += 1
                            if(j==m):
                                end2 = True
                # result = min(nums1[i],nums2[j])
        else:
            mid = int((n+m)/2)
            results = [0,0]
            index = 0
            if n==0:
                result = (nums2[mid]+nums2[mid-1])/2
            elif m == 0:
                result = (nums1[mid]+nums1[mid-1])/2
            else:
                end1 = False
                end2 = False
                for k in range(mid+1):
                    if end1:
                        results[index] = nums2[j]
                        j += 1
                    elif end2:
                        results[index] = nums1[i]
                        i += 1
                    else:
                        if nums1[i]<nums2[j]:
                            results[index] = nums1[i]
                            i += 1
                            if(i==n):
                                end1 = True
                        else:
                            results[index] = nums2[j]
                            j += 1
                            if(j==m):
                                end2 = True
                    index = 1 - index
                result = (results[0] + results[1])/2
        return result
# @lc code=end

