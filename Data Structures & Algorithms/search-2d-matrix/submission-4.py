class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## 1x Binary Search
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, (ROWS * COLS) - 1
        while L <= R:
            M = (L + R) // 2
            row, col = M // COLS,  M % COLS
            if matrix[row][col] < target:
                L = M + 1
            elif matrix[row][col] > target:
                R = M - 1
            else:
                return True
        return False


        ## 2x Binary Search
        # ROWS, COLS = len(matrix), len(matrix[0])
        # T, B = 0, ROWS - 1
        # row = None

        # while T <= B:
        #     M = (T + B) // 2
        #     if matrix[M][0] > target:
        #         B = M - 1
        #     elif matrix[M][-1] < target:
        #         T = M + 1
        #     else:
        #         row = M
        #         break

        # if row is None:
        #     return False

        # L, R = 0, COLS - 1
        # while L <= R:
        #     M = (L + R) // 2
        #     if matrix[row][M] > target:
        #         R = M - 1
        #     elif matrix[row][M] < target:
        #         L = M + 1
        #     else:
        #         return True
        # return False
