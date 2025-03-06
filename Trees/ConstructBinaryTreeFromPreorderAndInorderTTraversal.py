
"""
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:



Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
Example 2:

Input: preorder = [1], inorder = [1]

Output: [1]
Constraints:

1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000


"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
def buildTree(preorder, inorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
    root.right = buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])

    return root
# Time Complexity: O(n^2)

# Recursive with hashmap
def buildTree(preorder, inorder):
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_iter = iter(preorder)

    def helper(start, end):
        if start > end:
            return None

        root_val = next(preorder_iter)
        root = TreeNode(root_val)
        root_idx = inorder_map[root_val]

        root.left = helper(start, root_idx - 1)
        root.right = helper(root_idx + 1, end)

        return root

    return helper(0, len(inorder) - 1)
