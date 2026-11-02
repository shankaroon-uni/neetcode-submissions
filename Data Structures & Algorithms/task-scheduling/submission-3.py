from collections import deque 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0

        
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap)
        
        queue = deque()

        time = 0
        while heap or queue:
            
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append((cnt, n + time))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
                
        
            
        return time