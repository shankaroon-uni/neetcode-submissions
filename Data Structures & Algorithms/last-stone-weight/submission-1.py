import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            big = heapq.heappop(stones) * -1
            secondbig = heapq.heappop(stones) * -1

            if big != secondbig:
                diff = secondbig - big
                heapq.heappush(stones,diff)
        if len(stones) == 0:
            return 0
        return heapq.heappop(stones) * -1