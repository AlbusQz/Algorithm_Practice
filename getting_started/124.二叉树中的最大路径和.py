#
# @lc app=leetcode.cn id=124 lang=python
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        ###有点意思的，dfs+路径选择
        nodes = [-1001]
        def dfs(root):
            if root is None:
                return 0
            temp_l = dfs(root.left)
            temp_r = dfs(root.right)
            if temp_l < 0:
                temp_l = 0
            if temp_r < 0:
                temp_r = 0
            if root.val + temp_l + temp_r > nodes[-1]:
                nodes[-1] = root.val + temp_l + temp_r
            return root.val + max(temp_l,temp_r)
        dfs(root)
        return nodes[-1]

# @lc code=end

