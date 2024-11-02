#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ## 遍历法
        if root is None:
                return True
        def dfs(left,right):
            
            if left is None and right is None:
                return True
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left.val != right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        
        return dfs(root.left,root.right)
        
        ## 直接使用中根遍历会出现null和None分不清的情况
        '''
        nodes = []
        
        def mid_root(root):
            if root is None:
                # nodes.append(101)
                return
            if root.left is None and root.right is None:
                # nodes.append(101)
                nodes.append(root.val)
                # nodes.append(101)
                
            else:
                if root.left is not None:
                    mid_root(root.left)
                else:
                    nodes.append(-101)
                nodes.append(root.val)
                if root.right is not None:
                    mid_root(root.right)
                else:
                    nodes.append(-101)

        mid_root(root)
        n = len(nodes)
        print(nodes)

        l = 0
        r = n-1
        while l < r:
            if nodes[l] != nodes[r]:
                return False
            l += 1
            r -= 1
        return True
        '''        
# @lc code=end

