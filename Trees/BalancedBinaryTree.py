
"""
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: true
Example 2:



Input: root = [1,2,3,null,null,4,null,5]

Output: false
Example 3:

Input: root = []

Output: true

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
def isBalanced(root):
    
    def check(node):
        if not node:
            return 0
        left_height = check(node.left)
        right_height = check(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    return check(root) != -1


# Iterative
def isBalanced_iterative(root):
    if not root:
        return True

    stack = [root]
    mp = {None: 0}

    while stack:
        node = stack[-1]
        if node.left and node.left not in mp:
            stack.append(node.left)
        elif node.right and node.right not in mp:
            stack.append(node.right)
        else:
            node = stack.pop()
            left_height = mp[node.left]
            right_height = mp[node.right]
            height = max(left_height, right_height) + 1
            if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
                mp[node] = -1
            else:
                mp[node] = height
    return mp[root] != -1

