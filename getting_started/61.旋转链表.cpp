/*
 * @lc app=leetcode.cn id=61 lang=cpp
 *
 * [61] 旋转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {

        if(k == 0)
        {
            return head;
        }
        if(head == nullptr)
        {
            return head;
        }
        
        ListNode *temp_node = head;
        ListNode *pre;
        int n = 0;
        while (temp_node != nullptr)
        {
            pre = temp_node;
            temp_node = temp_node->next;
            n ++;
        }
        
        k = k % n;
        if(k == 0)
        {
            return head;
        }

        pre->next = head;
        int i = 0;
        temp_node = head;

        while(i + k <n)
        {
            i ++;
            pre = temp_node;
            temp_node = temp_node->next;
        }
        pre->next = nullptr;
        return temp_node;
        
    }
};
// @lc code=end

