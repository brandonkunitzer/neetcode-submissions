class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        vals = set()
        for right in range(len(s)):
            while s[right] in vals:
                vals.remove(s[left])
                left += 1
            vals.add(s[right])
            best = max(best, right - left + 1)
        return best

            
        