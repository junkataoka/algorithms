
"""
Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:



Input: root = [2,1,1,3,null,1,5]

Output: 3


Example 2:

Input: root = [1,2,-1,3,4]

Output: 4
Constraints:

1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive

def goodNodes(root: TreeNode) -> int:

    def dfs(node, max_val):
        if not node:
            return 0
        if node.val >= max_val:
            max_val = node.val
            return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(node.left, max_val) + dfs(node.right, max_val)

    return dfs(root, root.val)

# Iterative

def goodNodes(root: TreeNode) -> int:
    queue = [(root, root.val)]
    count = 0

    while queue:
        node, max_val = queue.pop()
        if not node:
            continue

        if node.val >= max_val:
            max_val = node.val
            count += 1

        queue.append((node.left, max_val))
        queue.append((node.right, max_val))

