class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        #if an O is on the edge leave it and it's region
        # if the O is not on the edge, find its region and replace it with Xs
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def dfs(row,col):
            visited.add((row,col))

            for x,y in directions:
                newRow = x + row
                newCol = y + col

                if 0 <= newRow < ROWS and 0 <= newCol < COLS and (newRow,newCol) not in visited and board[newRow][newCol] == "O":
                    visited.add((newRow,newCol))
                    dfs(newRow,newCol)

        #make all the 'O's on linked to the edge VISITED
        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][COLS-1] == "O":
                dfs(row,COLS-1)
        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0,col)
            if board[ROWS-1][col] == "O":
                dfs(ROWS-1,col)


        #go through the board and if the O has not been visited, change it to an X

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row,col) not in visited:
                    board[row][col] = "X"
