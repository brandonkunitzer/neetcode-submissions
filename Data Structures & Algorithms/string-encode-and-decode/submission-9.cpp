class Solution {
public:

    string encode(vector<string>& strs) {
        string lens;
        string words;
        for (const auto & str : strs) {
            lens += to_string(str.size()) + ",";
            words += str;
        }
        return lens + "]" + words;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int idx = s.find("]");
        string lens = s.substr(0, idx);
        string words = s.substr(idx + 1);
        int tracker = 0;
        while (tracker < lens.size()) {
            int comma_idx = s.find(",", tracker);
            int num = stoi(s.substr(tracker, comma_idx - tracker));
            res.push_back(words.substr(0, num));
            words = words.substr(num);
            tracker = comma_idx + 1;
        }
        return res;
    }
};
