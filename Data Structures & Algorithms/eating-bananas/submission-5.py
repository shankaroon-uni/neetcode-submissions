class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        answer = 0
        while l <= r:
            m = (l + r) // 2
            hours = 0
            for i in piles:
                hours += (i + m - 1) // m
            if hours > h:
                l = m + 1
            elif hours <= h:
                answer = m
                r = m - 1
        return answer