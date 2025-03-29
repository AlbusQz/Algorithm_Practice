/*
 * @lc app=leetcode.cn id=238 lang=cpp
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> result = {1};
        int n = nums.size();

        for(int i = 0; i < n - 1; i++)
        {
            result.push_back(result[i] * nums[i]);
        }

        int r = 1;

        for(int i = n-1; i > -1; i--)
        {
            result[i] = r * result[i];
            r = r * nums[i];
        }
        
        return result;

    }
};
// @lc code=end

