class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)]
        hashmap = defaultdict(int)
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for key, value in hashmap.items():
            buckets[value].append(key)
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for y in buckets[i]:
                result.append(y)
            if len(result) == k:
                return result

