"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.

Example 1:



Input: n = 4

Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There are two different solutions to the 4-queens puzzle.

Example 2:

Input: n = 1

Output: [["Q"]]
"""

def solveNQueens(n):
    col = set()
    pos_diag = set()
    neg_diag = set()
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def backtrack(row):
        if row == n:
            res.append([''.join(row) for row in board])
            return
        
        for i in range(n):
            if i in col or (row + i) in pos_diag or (row - i) in neg_diag:
                continue

            col.add(i)
            pos_diag.add(row + i)
            neg_diag.add(row - i)
            board[row][i] = 'Q'

            backtrack(row + 1)

            col.remove(i)
            pos_diag.remove(row + i)
            neg_diag.remove(row - i)
            board[row][i] = '.'
