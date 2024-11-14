#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(p,q):
            
            if p is None and q is not None:
                return False
            elif q is None and p is not None:
                return False
            elif p is None and q is None:
                return True
            else:
                if p.val != q.val:
                    return False
                return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)
        
# @lc code=end

