"""
You are given a square 2-D matrix of distinct integers grid where each integer grid[i][j] represents the elevation at position (i, j).

Rain starts to fall at time = 0, which causes the water level to rise. At time t, the water level across the entire grid is t.

You may swim either horizontally or vertically in the grid between two adjacent squares if the original elevation of both squares is less than or equal to the water level at time t.

Starting from the top left square (0, 0), return the minimum amount of time it will take until it is possible to reach the bottom right square (n - 1, n - 1).

Example 1:



Input: grid = [[0,1],[2,3]]

Output: 3
Explanation: For a path to exist to the bottom right square grid[1][1] the water elevation must be at least 3. At time t = 3, the water level is 3.

Example 2:



Input: grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]]
]

Output: 8
Explanation: The water level must be at least 8 to reach the bottom right square. The path is [0, 1, 2, 4, 8, 7, 6].

Constraints:

grid.length == grid[i].length
1 <= grid.length <= 50
0 <= grid[i][j] < n^2
"""

def swiminwater(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    # Min-heap priority queue with (max height so far, row, col)
    pq = [(grid[0][0], 0, 0)]
    visited = {(0, 0)}
    
    while pq:
        height, r, c = heapq.heappop(pq)
        
        # If we reached the bottom right, return the result
        if r == rows - 1 and c == cols - 1:
            return height
        
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited):
                visited.add((nr, nc))
                # The max height is either the current height or the new cell's height
                new_height = max(height, grid[nr][nc])
                heapq.heappush(pq, (new_height, nr, nc))
    
    return -1  # Unreachable in this problem

