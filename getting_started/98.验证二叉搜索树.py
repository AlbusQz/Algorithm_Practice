#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        output = []
        def midRoot(root):
            if root is None:
                return 
            midRoot(root.left)
            output.append(root.val)
            midRoot(root.right)
        midRoot(root)
        n = len(output)
        # print(output)
        for i in range(0,n-1):
            if output[i] >= output[i+1]:
                return False
        return True
# @lc code=end

