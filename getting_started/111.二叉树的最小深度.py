#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def getDepth(root):
            if root.left is None and root.right is None:
                return 1
            elif root.left is None:
                return getDepth(root.right) + 1
            elif root.right is None:
                return getDepth(root.left) + 1
            else:
                return 1 + min(getDepth(root.left),getDepth(root.right))
        return getDepth(root) 
# @lc code=end

