class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = float("-inf")
        for num in nums:
            if num - 1 not in nums:
                total = 1
                curr = num + 1
                while curr in nums:
                    total += 1
                    curr += 1
                best = max(best, total)
        return max(best, 0)