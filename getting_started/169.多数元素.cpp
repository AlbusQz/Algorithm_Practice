/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */

// @lc code=start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int n = nums.size();
        int can = nums[0];
        int count = 1;
        for(int i = 1;i< n; i++)
        {
            if(count == 0)
            {
                can = nums[i];
            }
            if(can == nums[i])
            {
                count ++;
            }
            else
            {
                count --;
            }
        }

        return can;

    }
};
// @lc code=end

