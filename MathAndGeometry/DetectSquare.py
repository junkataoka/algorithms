"""
You are given a stream of points consisting of x-y coordinates on a 2-D plane. Points can be added and queried as follows:

Add - new points can be added to the stream into a data structure. Duplicate points are allowed and should be treated as separate points.
Query - Given a single query point, count the number of ways to choose three additional points from the data structure such that the three points and the query point form a square. The square must have all sides parallel to the x-axis and y-axis, i.e. no diagonal squares are allowed. Recall that a square must have four equal sides.
Implement the CountSquares class:

CountSquares() Initializes the object.
void add(int[] point) Adds a new point point = [x, y].
int count(int[] point) Counts the number of ways to form valid squares with point point = [x, y] as described above.
Example 1:



Input: 
["CountSquares", "add", [[1, 1]], "add", [[2, 2]], "add", [[1, 2]], "count", [[2, 1]], "count", [[3, 3]], "add", [[2, 2]], "count", [[2, 1]]]
       
Output:
[null, null, null, null, 1, 0, null, 2]

Explanation:
CountSquares countSquares = new CountSquares();
countSquares.add([1, 1]);
countSquares.add([2, 2]);
countSquares.add([1, 2]);

countSquares.count([2, 1]);   // return 1.
countSquares.count([3, 3]);   // return 0.
countSquares.add([2, 2]);     // Duplicate points are allowed.
countSquares.count([2, 1]);   // return 2. 
Constraints:

point.length == 2
0 <= x, y <= 1000
"""


from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: list[int]) -> None:
        self.ptsCount(tuple(point)) += 1 # Store the count of each point in a dictionary
        self.pts.append(point)

    def count(self, point: list[int]) -> int:

        res = 0
        px, py = point

        for x, y in self.pts:

            if (abs(px - x) != abs(py - y)) or (px == x or py == y):
                # Skip if the point is not forming a square with the query point
                continue
            # Calculate the other two points of the square
            p1 = (px, y)
            p2 = (x, py)
            # Check if the other two points exist in the data structure
            res += self.ptsCount[p1] * self.ptsCount[p2]

        return res
        
