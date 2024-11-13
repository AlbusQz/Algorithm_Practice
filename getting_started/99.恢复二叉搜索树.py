#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        ## O(n)空间复杂度方法
        output = []
        nodes = {}
        def midRoot(root):
            if root is None:
                return 
            midRoot(root.left)
            output.append(root.val)
            nodes[root.val] = root
            midRoot(root.right)
        midRoot(root)
        n = len(output)
        for i in range(0,n-1):
            if output[i] >= output[i+1]:
                max_output = max(output[:i+1])
                min_output = min(output[i+1:])
                nodes[min_output].val = max_output
                nodes[max_output].val = min_output
                break
        return 
# @lc code=end

