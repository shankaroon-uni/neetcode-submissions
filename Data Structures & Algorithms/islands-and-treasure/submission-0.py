
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()

        q = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    seen.add((row,col))
                    q.append((row,col))

        while q:
            row,col = q.popleft()
            
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for x,y in directions:
                newRow = x + row
                newCol = y + col

                if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == 2147483647 and (newRow,newCol) not in seen:

                    grid[newRow][newCol] = grid[row][col] + 1
                    seen.add((newRow,newCol))
                    q.append((newRow,newCol))
 