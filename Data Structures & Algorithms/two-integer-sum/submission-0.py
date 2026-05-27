class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx in range(len(nums)):
            need = target - nums[idx]
            if need in seen:
                return [seen[need], idx]
            seen[nums[idx]] = idx
        