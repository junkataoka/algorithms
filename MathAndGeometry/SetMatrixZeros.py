"""
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:



Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:

1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1

"""


def setZeroes(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    first_row_has_zero = any(matrix[0][j] == 0 for j in range(COLS))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(ROWS))
    
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(1, ROWS):
        if matrix[r][0] == 0:
            for c in range(1, COLS):
                matrix[r][c] = 0

    for c in range(1, COLS):
        if matrix[0][c] == 0:
            for r in range(1, ROWS):
                matrix[r][c] = 0

    if first_row_has_zero:
        for c in range(COLS):
            matrix[0][c] = 0

    if first_col_has_zero:
        for r in range(ROWS):
            matrix[r][0] = 0

