#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        queue = [root]
        result = []
        while len(queue) > 0:
            temp_queue = []
            temp_result = []
            for i in queue:
                
                if i is None:
                    continue
                temp_result.append(i.val)
                temp_queue.append(i.left)
                temp_queue.append(i.right)
            if len(temp_result) > 0:
                result.append(temp_result)
            del queue
            queue = temp_queue
        return result    
            
# @lc code=end

