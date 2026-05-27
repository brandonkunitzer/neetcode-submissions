class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        map<char, int> counts;
        for (char ch : s) {
            counts[ch] ++;
        }
        for (char ch : t) {
            if (counts.contains(ch) & counts[ch] > 0) {
                counts[ch] --;
            } else {
                return false;
            }
        }
        return true;
    }
};
