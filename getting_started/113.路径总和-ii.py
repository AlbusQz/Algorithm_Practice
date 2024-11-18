#
# @lc app=leetcode.cn id=113 lang=python
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        def findPath(root,path):
            path.append(root.val)
            if root.left is None and root.right is None:
                if sum(path) == targetSum:
                    result.append((path))
                else:
                    return
            elif root.left is not None and root.right is None:
                findPath(root.left,copy.copy(path))
            elif root.right is not None and root.left is None:
                findPath(root.right,copy.copy(path))
            else:
                findPath(root.left,copy.copy(path))
                findPath(root.right,copy.copy(path))
        findPath(root,[])
        return result
# @lc code=end

