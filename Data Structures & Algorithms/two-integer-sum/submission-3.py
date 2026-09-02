class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            newTarget = target - val
            if newTarget in seen:
                return [seen[newTarget], i]
            else:
                seen[val] = i