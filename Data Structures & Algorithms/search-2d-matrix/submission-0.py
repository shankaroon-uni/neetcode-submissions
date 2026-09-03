class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1
        columns = len(matrix[0])
        while l <= r:
            m = (r + l) // 2
            middle = matrix[m//columns][m%columns]
            if middle > target:
                r = m - 1
            elif middle < target:
                l = m + 1
            else:
                return True
        return False

        