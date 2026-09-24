class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        added = False
        for interval in intervals:
            if added:
                res.append(interval)
            elif interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                res.append(newInterval)
                res.append(interval)
                added = True
            else:
                newInterval = [min(newInterval[0],interval[0]), max(newInterval[1], interval[1])]
            
        if not added:
            res.append(newInterval)

        
        return res