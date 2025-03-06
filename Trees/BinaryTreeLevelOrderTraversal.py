"""
Binary Tree Level Order Traversal
Solved 
Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
Example 2:

Input: root = [1]

Output: [[1]]
Example 3:

Input: root = []

Output: []
Constraints:

0 <= The number of nodes in both trees <= 1000.
-1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative
def levelOrder(root):
    if not root:
        return []
    res = []
    queue = [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

# Recursive BFS
def levelOrder_recursive(root):
    """
         3
        / \
       9  20
         /  \
        15   7
    The execution would go like this:

    Start with res = []
    Process root (3): Create res = [[3]]
    Process level 1: Create res = [[3], [9,20]]
    Process level 2: Create res = [[3], [9,20], [15,7]]

    Final result: [[3], [9,20], [15,7]]

    """
    res = []
    def helper(node, level):
        if not node:
            return
        if len(res) == level:
            res.append([]) # Create new sublist for this level if it doesn't exist
        res[level].append(node.val)

        helper(node.left, level + 1)
        helper(node.right, level + 1)

    helper(root, 0)
    return res


