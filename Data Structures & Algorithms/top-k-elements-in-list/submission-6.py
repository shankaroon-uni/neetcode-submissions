class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for i in nums:
            seen[i] = seen.get(i, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in seen.items():
            buckets[freq].append(num)

        output = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(output) == k:
                    return output
                output.append(num)
        return output
