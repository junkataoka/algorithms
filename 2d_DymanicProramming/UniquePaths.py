"""
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:



Input: m = 3, n = 6

Output: 21
Example 2:

Input: m = 3, n = 3

Output: 6
Constraints:

1 <= m, n <= 100

"""
def uniquePaths(m: int, n: int) -> int:
    ROWS = m
    COLS = n
    memo = {}

    def dfs(r, c):

        if (r == ROWS - 1 and c == COLS - 1):
            return 1

        if r >= ROWS or c >= COLS:
            return 0

        if (r, c) in memo:
            return memo[(r, c)]
        
        memo[(r, c)] = dfs(r, c + 1) + dfs(r + 1, c)

        return memo[(r, c)]       

    return dfs(0, 0)
            

