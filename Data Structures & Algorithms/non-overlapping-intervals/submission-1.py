class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        overlap = []
        for i in range(len(intervals)):
            if len(overlap) == 0:
                overlap.append(intervals[i])
            elif intervals[i][0] >= overlap[-1][1]:
                overlap.append(intervals[i])
            else:
                last = overlap.pop()
                if last[1] > intervals[i][1]:
                    overlap.append(intervals[i])
                else:
                    overlap.append(last)

        return len(intervals) - len(overlap)