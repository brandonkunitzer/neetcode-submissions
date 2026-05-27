class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            curr = tuple(sorted(Counter(s).items()))
            if curr not in seen:
                seen[curr] = []
            seen[curr].append(s)
        return list(seen.values())