#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        queue = [root]
        while len(queue) > 0:
            temp_result = []
            temp_queue = []
            for i in queue:
                if i is None:
                    continue
                temp_result.append(i.val)
                temp_queue.append(i.left)
                temp_queue.append(i.right)
            del queue
            queue = temp_queue
            if len(temp_result) > 0:
                result.insert(0,temp_result)
                
        return result
# @lc code=end

