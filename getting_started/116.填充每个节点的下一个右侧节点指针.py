#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        queue = [root]
        while len(queue) >0:
            temp_queue = []
            for i in range(len(queue)):
                node = queue[i]
                if i < len(queue) - 1:
                    node.next = queue[i+1]
                if node.left is not None:
                    temp_queue.append(node.left)
                if node.right is not None:
                    temp_queue.append(node.right)
            queue = temp_queue
        return  root     
        
# @lc code=end

