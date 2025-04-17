"""
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3]

Output: [1,3]
Example 2:

Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
Constraints:

0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

"""


def rightSideView(root):

    result = []

    def dfs(node, level):
        if not node:
            return

        if level == len(result):
            result.append(node.val)

        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    dfs(root, 0)
    return result
