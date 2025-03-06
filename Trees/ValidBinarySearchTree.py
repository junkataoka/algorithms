
"""
Valid Binary Search Tree
Solved 
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3]

Output: true
Example 2:



Input: root = [1,2,3]

Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

Constraints:

1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def isValidBST(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, float('-inf'), float('inf'))



def isValidBST(root):
    queue = collections.deque([(root, float('-inf'), float('inf'))])

    while queue:
        node, min_val, max_val = queue.popleft()
        if not node:
            continue

        if node.val <= min_val or node.val >= max_val:
            return False

        queue.append((node.left, min_val, node.val))
        queue.append((node.right, node.val, max_val))

    return True
