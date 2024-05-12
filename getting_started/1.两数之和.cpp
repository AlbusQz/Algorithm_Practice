// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include <unordered_map>
#include "commoncppproblem1.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
// #include <vector>
// using namespace std;
class Solution {
public:
    // brute force
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     int n = nums.size();
    //     vector<int> result;
    //     for(int i = 0;i<n;i++)
    //     {
    //         for (int j = i+1; j<n;j++)
    //         {
    //             if(nums[i]+nums[j]==target)
    //             {
    //                 result.push_back(i);
    //                 result.push_back(j);
    //                 break;
    //             }
    //         }
    //     }
    //     return result;
    // }
    
    //hash table
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> result;
        unordered_map<int,int> hash_table;
        for(int i = 0;i<n;i++)
        {
           if(hash_table.find(target-nums[i])!=hash_table.end())
           {
                result.push_back(hash_table[target-nums[i]]);
                result.push_back(i);
                break;
           }
           else
           {
                hash_table[nums[i]] = i;
           }
        }
        return result;
    }

};
// @lc code=end

