class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> contains(nums.begin(), nums.end());

        int best = 0;
        for (const auto & num : nums) {
            if (contains.contains(num - 1)) {
                continue;
            }
            int curr_len = 1;
            int curr_num = num;
            while (contains.contains(curr_num + 1)) {
                curr_num ++;
                curr_len ++;
            }
            best = max(curr_len, best);
        }
        return best;
    }
};
