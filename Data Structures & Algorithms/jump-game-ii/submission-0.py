class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        maxStep = 0
        n = len(nums)
        currentEnd = 0

        for i in range(n - 1):
            maxStep = max(maxStep, nums[i] + i)

            if i == currentEnd:
                count += 1
                currentEnd = maxStep
            
        return count