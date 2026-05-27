class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }
        vector<vector<int>> vals;
        for (const auto& pair : counts) {
            // vector<int> curr = {pair.first, pair.second}
            vals.push_back({pair.first, pair.second});
        }
        sort(vals.begin(), vals.end(), [](vector<int> & a, vector<int> & b) {
            return a[1] > b[1];
        });
        vector<int> res;
        for (int i = 0; i < k ; i++) {
            res.push_back(vals[i][0]);
        }
        return res;
    }
};
