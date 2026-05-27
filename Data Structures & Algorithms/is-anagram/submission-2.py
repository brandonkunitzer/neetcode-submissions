class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        contains = Counter(s.lower())
        for char in t.lower():
            if char in contains:
                if contains[char] == 0:
                    return False
                contains[char] -= 1
            else:
                return False
        return True
