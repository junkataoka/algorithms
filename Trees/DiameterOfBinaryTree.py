"""
The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:



Input: root = [1,null,2,3,4,5]

Output: 3
Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
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
def diameterOfBinaryTree(root):
    diameter = [0]

    def get_depth(node):
        if not node:
            return 0
        left_depth = get_depth(node.left)
        right_depth = get_depth(node.right)
        diameter[0] = max(diameter[0], left_depth + right_depth)
        return max(left_depth, right_depth) + 1

    get_depth(root)

    return diameter[0]

# Iterative
def diameterOfBinaryTree_iterative(root):
    stack = [root]
    mp = {None: (0, 0)}

    while stack:
        node = stack[-1]
        if node.left and node.left not in mp: # If left node is not in the map
            stack.append(node.left) 
        elif node.right and node.right not in mp: # If right node is not in the map
            stack.append(node.right)

        else: # If both left and right nodes are in the map (This is the case when we have visited both left and right nodes, so we can calculate the depth and diameter of the current node)
            node = stack.pop()
            left_height, left_diameter = mp[node.left]
            right_height, right_diameter = mp[node.right]

            height = max(left_height, right_height) + 1
            diameter = max(left_height + right_height, left_diameter, right_diameter)

            mp[node] = (height, diameter)

    return mp[root][1]
