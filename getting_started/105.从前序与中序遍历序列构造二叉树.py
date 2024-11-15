#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        n = len(preorder)
        preorder_index = {}
        inorder_index = {}
        used = {}
        for i in range(n):
            preorder_index[preorder[i]] =i
            inorder_index[inorder[i]] = i
            used[inorder[i]] = False
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        def bulidTree(root):
            if root is None:
                return 
            val = root.val
            pre_i = preorder_index[val]
            in_iu = inorder_index[val]
            i = pre_i + 1
            if i < n:
                temp_val = preorder[i]
                temp_in = inorder_index[temp_val]
                if used[temp_val] == False and temp_in < in_iu:
                    temp = TreeNode(temp_val)
                    root.left = temp
                    used[temp_val] = True
                    i += 1
            while i < n:
                temp_val = preorder[i]
                temp_in = inorder_index[temp_val]
                if used[temp_val] == True:
                    break
                elif used[temp_val] == False and temp_in > in_iu:
                    temp = TreeNode(temp_val)
                    root.right = temp
                    used[temp_val] = True
                    break
                i += 1
            bulidTree(root.left)
            bulidTree(root.right)
        
        bulidTree(root)
        return root
        
# @lc code=end

