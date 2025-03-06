"""
You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

Example 1:



Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

Output: 3
Example 2:

Input: times = [[1,2,1],[2,3,1]], n = 3, k = 2

Output: -1
Constraints:

1 <= k <= n <= 100

"""

def networkDelayTime(times, n, k):
    import heapq
    import collections
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    visited = set()

    q = [(0, k)]
    while q:
        time, node = heapq.heappop(q)
        if node in visited:
            continue
        visited.add(node)
        if len(visited) == n:
            return time
        if node in graph:
            for v, w in graph[node]:
                if v not in visited:
                    heapq.heappush(q, (time + w, v))
    return -1

# Time Complexity: O(NlogN + E), where N is the number of nodes in the graph, and E is the number of edges in the graph.
# Reasoning: We visit every node once, and every edge once.
