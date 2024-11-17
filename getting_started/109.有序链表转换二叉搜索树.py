#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        if head is None:
            return None
        List = []
        while head is not None:
            List.append(head.val)
            head = head.next
        n = len(List)
        def bulidBST(left,right):
            if left == right:
                return TreeNode(List[left])
            mid = int((left+right)/2)
            root = TreeNode(List[mid])
            if mid > left:
                root.left = bulidBST(left,mid-1)
            if mid < right:
                root.right = bulidBST(mid+1, right)
            return root
        return bulidBST(0,n-1)
            
# @lc code=end

