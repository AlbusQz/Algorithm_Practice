#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n = len(inorder)
        if n == 0:
            return None
        
        in_index = {}
        post_index = {}
        visited = []
        for i in range(n):
            in_index[inorder[i]] = i
            post_index[postorder[i]] = i
            visited.append(False)
        
        root = TreeNode(postorder[-1])
        root_in = in_index[postorder[-1]]
        visited[root_in] = True
        
        def bulidTree(root):
            if root is None:
                return 
            val = root.val
            root_in = in_index[val]
            root_post = post_index[val]
            
            l_post = root_post - 1
            while l_post > -1:
                l_val = postorder[l_post]
                l_in = in_index[l_val]
                if visited[l_in] == False and l_in < root_in:
                    left = TreeNode(l_val)
                    root.left = left
                    visited[l_in] = True
                    break
                l_post -= 1

            r_post = root_post - 1
            if r_post > -1:
                r_val = postorder[r_post]
                r_in = in_index[r_val]
                if visited[r_in] == False and r_in > root_in:
                    right = TreeNode(r_val)
                    root.right = right
                    visited[r_in] = True
            
            bulidTree(root.left)
            bulidTree(root.right)
             
        bulidTree(root)
        return root
            
# @lc code=end

