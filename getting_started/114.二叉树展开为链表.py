#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        def bulidList(root):
            if root.left is None and root.right is None:
                return root,root
            elif root.left is not None and root.right is None:
                head,tail = bulidList(root.left)
                root.right = head
                root.left = None
                return root,tail
            elif root.right is not None and root.left is None:
                head,tail = bulidList(root.right)
                return root,tail
            else:
                l_head,l_tail = bulidList(root.left)
                r_head,r_tail = bulidList(root.right)
                l_tail.left = None
                l_tail.right = r_head
                root.right = l_head
                root.left = None
                return root,r_tail
        bulidList(root)
            
# @lc code=end

