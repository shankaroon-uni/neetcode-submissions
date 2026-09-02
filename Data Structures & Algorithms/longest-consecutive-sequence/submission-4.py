class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_count = 0

        count = 1

        for i in numbers:
            if (i-1) not in numbers:
                current_num = i
                current_count = 1
                while (current_num + 1) in numbers:
                    current_num += 1
                    current_count += 1
                if current_count > max_count:
                    max_count= current_count

        return max_count
