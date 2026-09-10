from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        q = deque()
        rows, columns = len(grid), len(grid[0])
        visited = set()
        directions = [[0,-1], [0,1], [1,0], [-1,0]]

        def bfs(r,c):
            q.append((r,c))
            while q:
                (r,c) = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(rows) and col in range(columns) and grid[row][col] == "1" and (row, col) not in visited:
                        visited.add((row,col))
                        q.append((row,col))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands