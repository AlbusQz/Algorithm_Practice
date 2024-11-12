#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
       
        def buildTree(left,i,right):
            temp_node = TreeNode()
            temp_node.val = i
            if left == right:
                return 1,[temp_node]
            l = 0
            left_nodes = []
            for j in range(left,i):
                temp_l,temp_left_nodes = buildTree(left,j,i-1)
                l += temp_l
                left_nodes += temp_left_nodes
            r = 0
            right_nodes = []
            for j in range(i+1,right+1):
                temp_r,temp_right_nodes = buildTree(i+1,j,right)
                r += temp_r
                right_nodes += temp_right_nodes
            temp_result = []
            
            if l == 0 and right == 0:
                return 1,temp_node
            if l == 0:
                left_nodes = [None]
                l = 1
            if r == 0:
                right_nodes = [None]
                r = 1
                
            for p in range(l):
                for q in range(r):
                    root = copy.copy(temp_node)
                    root.left = left_nodes[p]
                    root.right = right_nodes[q]
                    temp_result.append(root)

            return len(temp_result),temp_result

        result = []
        for i in range(1,n+1):
            temp,temp_result = buildTree(1,i,n)
            result += temp_result
        return result
                

            
        
# @lc code=end

