import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        inv = {}
        for key, val in counts.items():
            if val not in inv:
                inv[val] = []
            inv[val].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            if len(res) < k:
                print(i, inv)
                if i in inv:
                    res += inv[i]
            else:
                return res
        return res

