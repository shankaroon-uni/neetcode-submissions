class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #check each row
        for row in board:
            check = set()
            for number in row:
                if number in check and number != ".":
                    return False
                check.add(number)

        #check each column
        for i in range(9):
            check2 = set()
            for j in range(9):
                number = board[j][i]
                if number in check2 and number != ".":
                    return False
                check2.add(number)

        #check each 3x3 square of 9
        
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                check3 = set()
                for i in range(3):
                    for j in range(3):
                        number = board[x+i][y+j]
                        if number in check3 and number != ".":
                            return False
                        check3.add(number)
        return True

