class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = str(sorted(word))
            if key not in seen:
                seen[key] = []
            seen[key].append(word)
        return [seen[key] for key in seen.keys()]