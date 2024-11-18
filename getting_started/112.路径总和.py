#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        def findPath(root,now_sum):
            now_sum = root.val + now_sum
            if root.left is None and root.right is None:
                if now_sum == targetSum:
                    return True
                else:
                    return False
            elif root.left is None and root.right is not None:
                return findPath(root.right,now_sum)
            elif root.left is not None and root.right is None:
                return findPath(root.left,now_sum)
            else:
                return findPath(root.left,now_sum) or findPath(root.right,now_sum)
        return findPath(root,0)
        
# @lc code=end

