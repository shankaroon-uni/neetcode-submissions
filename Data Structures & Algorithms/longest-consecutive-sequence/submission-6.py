class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_count = 0
        for i in numbers:
            if (i-1) not in numbers:
                current_count = 1
                current_num = i
                while current_num + 1 in numbers:
                    current_count += 1
                    current_num += 1
                max_count = max(current_count, max_count)


        return max_count