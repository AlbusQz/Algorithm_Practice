#
# @lc app=leetcode.cn id=129 lang=python
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        results =  []
        def dfs(root, val):
            if root is None:
                return 
            val = val *10 + root.val
            if root.left is None and root.right is None:
                results.append(val)
                return
            dfs(root.left,val)
            dfs(root.right,val)
            
        dfs(root,0)
        return sum(results)
        
# @lc code=end

