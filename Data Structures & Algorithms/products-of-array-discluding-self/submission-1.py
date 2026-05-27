class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = []
        curr = 1
        for num in nums:
            curr *= num
            mult.append(curr)
        res = []
        curr = 1
        for i in range(len(nums) - 1, 0, -1):
            res.append(curr * mult[i - 1])
            curr *= nums[i]
        res.append(curr)
        return list(reversed(res))