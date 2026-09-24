class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            if interval[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(interval[1], res[-1][1])]
            else:
                res.append(interval)

        return res