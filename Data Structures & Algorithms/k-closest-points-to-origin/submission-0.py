import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for c in points:
            x,y = c
            distance = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(heap,(distance, x , y))
        res = []
        for i in range(k):
            d , x , y = heapq.heappop(heap)
            res.append([x, y])
        return res