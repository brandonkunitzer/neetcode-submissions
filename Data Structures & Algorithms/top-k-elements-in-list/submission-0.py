import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        pq = []
        for key, val in counts.items(): 
            heapq.heappush(pq, (val, key))
            if len(pq) > k:
                heapq.heappop(pq)
        return [val[1] for val in pq]
