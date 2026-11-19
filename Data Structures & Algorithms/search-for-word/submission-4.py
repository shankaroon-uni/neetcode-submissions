class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        xBound = len(board)
        yBound = len(board[0])
        visited = set()

        def dfs(x,y,i):
            if board[x][y] != word[i]:
                return False
            if i == len(word) -1:
                return True

            directions = [[0,1], [1,0], [-1,0], [0,-1]]
            for u,d in directions:
                newX = x + u
                newY = y + d

                if 0 <= newX < xBound and 0 <= newY < yBound:
                    if board[newX][newY] == word[i+1] and (newX, newY) not in visited:

                        visited.add((newX,newY))
                        if not dfs(newX,newY, i+1):
                            visited.remove((newX,newY))
                        else:
                            return True

            return False


        for y in range(len(board[0])):
            for x in range(len(board)):
                if board[x][y] == word[0]:
                    visited.add((x,y))
                    if dfs(x,y,0):
                        return True
                    visited.remove((x,y))
        return False