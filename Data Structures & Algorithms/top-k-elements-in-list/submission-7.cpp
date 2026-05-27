class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counts;
        for (int num : nums) {
            counts[num]++;
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (const auto & pair : counts) {
            pq.push({pair.second, pair.first});
            if (pq.size() > k) {
                pq.pop();
            }
        }
        vector<int> res;
        while (pq.size() > 0){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};
