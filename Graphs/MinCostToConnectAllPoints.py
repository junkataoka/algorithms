"""
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:



Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
Constraints:

1 <= points.length <= 1000
-1000 <= xi, yi <= 1000

"""

# Prim's Algorithm
# Diffetent from Dijkstra's Algorithm, Prim's Algorithm is used to find the minimum spanning tree of a graph

def minCostConnectPoints(points):
    import heapq
    n = len(points)
    graph = {}
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append((j, dist))
            graph[j].append((i, dist))

    visited = set()
    q = [(0, 0)]
    res = 0
    while q:
        dist, node = heapq.heappop(q)
        if node in visited:
            continue
        visited.add(node)
        res += dist
        for v, w in graph[node]:
            if v not in visited:
                heapq.heappush(q, (w, v))
    return res

# Time Complexity: O(N^2logN), where N is the number of points in the graph.
