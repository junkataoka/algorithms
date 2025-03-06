"""
Given a node in a connected undirected graph, return a deep copy of the graph.

Each node in the graph contains an integer value and a list of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).

The input node will always be the first node in the graph and have 1 as the value.

Example 1:



Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]
Explanation: There are 3 nodes in the graph.
Node 1: val = 1 and neighbors = [2].
Node 2: val = 2 and neighbors = [1, 3].
Node 3: val = 3 and neighbors = [2].

Example 2:



Input: adjList = [[]]

Output: [[]]
Explanation: The graph has one node with no neighbors.

Example 3:

Input: adjList = []

Output: []
Explanation: The graph is empty.

Constraints:

0 <= The number of nodes in the graph <= 100.
1 <= Node.val <= 100
There are no duplicate edges and no self-loops in the graph.
"""

# Recursive DFS

def cloneGraph(node):
    oldToNew = {}
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]

        newNode = Node(node.val)
        oldToNew[node] = newNode
        newNode.neighbors = [dfs(neighbor) for neighbor in node.neighbors]
        return newNode

# Iterative BFS

def cloneGraph(node):
    if not node:
        return node

    oldToNew = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        for neighbor in curr.neighbors:
            if neighbor not in oldToNew:
                oldToNew[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            oldToNew[curr].neighbors.append(oldToNew[neighbor])

    return oldToNew[node]
