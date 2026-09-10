class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        turns = 0
        start = "0000"
        directions = [-1, 1]
        deadends = set(deadends)
        visited = set()
        q = deque()

        if start == target:
            return turns
        if start  in deadends:
            return -1
        
        q.append(start)
        visited.add(start)

        while q:
            turns += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(len(lock)):
                    for d in directions:
                        digit = str((int(lock[i]) + d + 10) % 10)
                        new_lock = lock[:i] + digit + lock[i+1:]
                        if new_lock not in visited and new_lock not in deadends:
                            q.append(new_lock)
                            visited.add(new_lock)
                        if new_lock == target:
                            return turns
        return -1

        