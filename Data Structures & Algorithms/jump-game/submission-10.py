class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_value = len(nums) - 1
        max_jump = 0
        for i in range(last_value + 1):
            if i > max_jump:
                return False
            max_jump = max(nums[i] + i, max_jump)
            
            if max_jump >= last_value:
                return True
            
