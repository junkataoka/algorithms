"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

"""

def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Treat the matrix as a flattened sorted array
    left = 0
    right = rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert the 1D index to 2D coordinates
        # row = mid // cols, col = mid % cols
        midValue = matrix[mid // cols][mid % cols]
        
        if midValue == target:
            return True
        elif midValue < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
