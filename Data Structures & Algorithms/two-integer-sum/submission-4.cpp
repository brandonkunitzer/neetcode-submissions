class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> seen;
        for (int i = 0; i < nums.size(); i ++) {
            int num = nums[i];
            if (seen.contains(target - num)) {
                return {seen[target - num], i};
            }
            seen[num] = i;
        }
    }
};
