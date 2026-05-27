class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> contains;
        for (const auto & num : nums) {
            contains.insert(num);
        }
        map<int, int> lens;
        int best = 0;
        for (const auto & num : nums) {
            if (lens.contains(num)) {
                continue;
            }
            int curr_len = 1;
            int curr_num = num;
            while (contains.contains(curr_num + 1)) {
                if (lens.contains(curr_num + 1)) {
                    curr_len += lens[curr_num + 1];
                    break;
                }
                curr_num ++;
                curr_len ++;
            }
            best = max(curr_len, best);
            lens[num] = curr_len, lens[num];
        }
        return best;
    }
};
