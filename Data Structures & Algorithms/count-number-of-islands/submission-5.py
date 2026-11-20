class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        rowBound = len(grid)
        colBound = len(grid[0])

        def dfs(row, col):
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for x,y in directions:
                newRow = row + x
                newCol = col + y
                if 0 <= newRow < rowBound and 0 <= newCol < colBound and grid[newRow][newCol] == "1" and (newRow,newCol) not in visited:
                    visited.add((newRow,newCol))
                    dfs(newRow,newCol)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1" and (x,y) not in visited:
                    visited.add((x,y))
                    dfs(x, y)
                    islands += 1 

        return islands