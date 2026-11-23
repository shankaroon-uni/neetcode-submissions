class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxRows = len(grid)
        maxColumns = len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(row, col):
            area = 1
            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            visited.add((row,col))

            for x,y in directions:
                newRow = row + x
                newCol = col + y

                if 0 <= newRow < maxRows and 0 <= newCol < maxColumns and (newRow,newCol) not in visited and grid[newRow][newCol] == 1:
                    visited.add((newRow,newCol))
                    area += dfs(newRow,newCol)
                     
            return area
            
        for row in range(maxRows):
            for col in range(maxColumns):
                if grid[row][col] == 1 and (row,col) not in visited:
                    newArea = dfs(row,col)
                    maxArea = max(maxArea,newArea)

        return maxArea
