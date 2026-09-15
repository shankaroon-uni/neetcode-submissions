class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        i = 0
        maxSpot = 0
        while i <= last:
            maxSpot = max(nums[i] + i, maxSpot)
            i += 1
            if maxSpot >= last:
                return True
            if i > maxSpot:
                return False            
