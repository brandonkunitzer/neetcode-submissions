class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        left[0] = nums[0]
        for i in range(1, len(nums)):
            left[i] *= left[i - 1] * nums[i]
        total = 1
        res = [1] * len(nums)
        for i in range(len(nums) - 1, 0, -1):
            res[i] = left[i - 1] * total
            total *= nums[i]
        res[0] = total
        return res

    
