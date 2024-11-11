#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(root):
            if root is None:
                return
            if root.left is not None:
                dfs(root.left)
            result.append(root.val)
            if root.right is not None:
                dfs(root.right)
        
        dfs(root)
        return result
# @lc code=end

