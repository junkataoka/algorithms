"""
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

# DFS
def countComponents(n, edges):
    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    for i in range(n):
        if i not in visited:
            count += 1
            dfs(i)
    return count

# Union Find

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]

        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]

        return True

def countComponents(n, edges):
    uf = UnionFind(n)
    res = n
    for u, v in edges:
        if uf.union(u, v):
            res -= 1

    return res

# I'd like to start simpler model to complex
# Deliver results
# Disagree and commit
# Simple model to complex
# Work backwards from customor problem
# Customer obsession, (Engage customers)
# Balance complexity and simplicity
# Ownership, (Ownership)
# AWS 
# How each realtes to forecasting
# What they do, network capacity
# Tell me a time your work with a team
# How would you handle conflict
