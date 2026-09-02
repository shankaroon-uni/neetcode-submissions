class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while end > start:
            ans = numbers[start] + numbers[end] 
            if ans == target:
                return [start + 1, end + 1]
            
            elif ans < target:
                start += 1
            elif ans > target:
                end -= 1
            