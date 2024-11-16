#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        n = len(nums)
        visited = [False for _ in range(n)]
        def bulidAVLBST(left,right):
            if left == right:
                return TreeNode(nums[left])
            mid = int((left + right)/2)
            root = TreeNode(nums[mid])
            if mid > left:
                root.left = bulidAVLBST(left,mid-1)
            if mid < right:
                root.right = bulidAVLBST(mid+1,right)
            return root
        return bulidAVLBST(0,n-1)
# @lc code=end

