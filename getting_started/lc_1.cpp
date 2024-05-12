#include <iostream>
#include <vector>
#include <list>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    // vector<int> twoSum(vector<int>& nums, int target) {
    //     vector<int> result;
    //     int n = nums.size();
    //     for(int i = 0;i<n;++i)
    //     {
    //         for(int j = i+1; j<n;++j)
    //         {
    //             int a = nums[i];
    //             int b = nums[j];
    //             if(nums[i]+nums[j]==target)
    //             {
    //                 cout<<i<<endl;
    //                 cout<<j;
    //                 result.push_back(i);
    //                 result.push_back(j);
    //                 return result;
    //             }
    //         }
    //     }
    //     return result;
    // }

     vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        vector<int> result;
        unordered_map<int,int> hash_table;
        for(int i = 0;i<n;i++)
        {
           if(hash_table.find(target-nums[i])!=hash_table.end())
           {
                result.push_back(i);
                result.push_back(hash_table[target-nums[i]]);
                break;
           }
           else
           {
                hash_table[hash_table[nums[i]]] = i;
           }
        }
    }
       
};


int main()
{
    vector<int> *nums = new vector<int>();
    nums->push_back(1);
    nums->push_back(2);
    nums->push_back(7);
    int target = 9;
    Solution *solution = new Solution();
    solution->twoSum(*nums,target);
    return 0;
}

