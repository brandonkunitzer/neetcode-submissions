class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> seen;
        for (string s : strs) {
            map<char, int> curr;
            for (char ch : s) {
                curr[ch] ++;
            }
            seen[curr].push_back(s);
        }
        vector<vector<string>> res;
        for (const auto & [key, val] : seen) {
            res.push_back(val);
        }
        return res;
    }   
};
