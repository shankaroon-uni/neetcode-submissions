class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        bucket = [[] for index in range(len(nums)+1)]
        for value, count in d.items():
            bucket[count].append(value)
        result = []
        
        for i in range(len(bucket)-1,0,-1):
            for x in bucket[i]:
                result.append(x)
                if len(result) == k:
                    return result
