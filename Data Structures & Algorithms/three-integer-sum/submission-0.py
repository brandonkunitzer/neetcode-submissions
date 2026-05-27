class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        has = {}
        for i in range(len(nums)):
            if nums[i] not in has:
                has[nums[i]] = set()
            has[nums[i]].add(i)
        for left in range(len(nums)):
            for right in range(len(nums)):
                if left != right:
                    need = -(nums[left] + nums[right])
                    if need in has:
                        tot_in = 0
                        if right in has[need]:
                            tot_in += 1
                        if left in has[need]:
                            tot_in += 1
                        if len(has[need]) > tot_in:
                            res.add(tuple(sorted((nums[left], nums[right], need))))
        return [list(x) for x in res]      
                        
