class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> mult;
        int curr = 1;
        for (const auto & num : nums) {
            curr *= num;
            mult.push_back(curr);
        }
        vector<int> res;
        int new_curr = 1;
        for (int i = nums.size() - 1; i > 0; i--) {
            res.push_back(new_curr * mult[i - 1]);
            new_curr *= nums[i];
        }
        res.push_back(new_curr);
        reverse(res.begin(), res.end());
        return res;
    }
};
