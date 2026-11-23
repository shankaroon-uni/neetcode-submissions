class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        ROWS = len(heights)
        COLS = len(heights[0])
        def dfs(row, col, visited):
            if (row, col) in visited:
                return
            visited.add((row, col))
            for x,y in directions:
                newRow = x + row
                newCol = y + col

                if 0 <= newRow < len(heights) and 0 <= newCol < len(heights[0]) and heights[newRow][newCol] >= heights[row][col] and (newRow, newCol) not in visited:
                    dfs(newRow, newCol, visited)

        for row in range(ROWS):
            dfs(row, 0, pacific)
            dfs(row, COLS - 1, atlantic)

        for col in range(COLS):
            dfs(0, col, pacific)
            dfs(ROWS - 1, col, atlantic)
        

        return [list(c) for c in pacific & atlantic]