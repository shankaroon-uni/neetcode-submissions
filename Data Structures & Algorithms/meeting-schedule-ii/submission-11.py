"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        roomEnds = []
        for i in range(len(intervals)):
            if len(roomEnds) == 0:
                heapq.heappush(roomEnds,intervals[i].end)
            else:
                first = heapq.heappop(roomEnds)
                if intervals[i].start >= first: 
                    heapq.heappush(roomEnds, intervals[i].end)
                    
                elif intervals[i].start < first: 
                    heapq.heappush(roomEnds, first)
                    heapq.heappush(roomEnds, intervals[i].end)

        return len(roomEnds)