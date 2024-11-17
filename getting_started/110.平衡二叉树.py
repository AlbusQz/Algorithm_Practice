#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isAVL(root):
            if root is None:
                return 0,True
            depth_l, flag_l = isAVL(root.left)
            depth_r, flag_r = isAVL(root.right)
            if flag_l is True and flag_r is True and abs(depth_l - depth_r)<= 1:
                flag = True
            else:
                flag = False
            depth = max(depth_l,depth_r) + 1
            return depth,flag
        depth, flag = isAVL(root)
        return flag
            
# @lc code=end

