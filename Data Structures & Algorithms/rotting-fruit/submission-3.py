from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh = 0

        time = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1

        directions = [[1,0],[0,1],[-1,0],[0,-1]]            
        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for x,y in directions:
                    newRow = x + row
                    newCol = y + col
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
                        fresh -= 1
            time += 1    

        return time if fresh == 0 else -1