/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */
// #include <unha>
// @lc code=start
class Solution {
public:

    int majorityElement(vector<int>& nums) {

        // Brute-Force, implement in cpp
        int n = nums.size();
        std::unordered_map<int,int> hashmap;

        for(int i = 0;i<n;i++)
        {
            int num = nums[i];
            if (hashmap.find(num) != hashmap.end()){
                hashmap[num] = hashmap[num] + 1;
            } 
            else{
                hashmap[num] = 1;
            }
            if(hashmap[num] > int(n/2))
                return num;
        }
        return -1;


        // Boyer-Moore 投票算法，Cpp实现
        /*
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
        */
    }
};
// @lc code=end

