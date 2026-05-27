class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = list(dict(Counter(nums)).items())
        counts.sort(key = lambda num : num[1])
        return [item[0] for item in counts[-k:]]
        
