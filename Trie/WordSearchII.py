"""

"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def findWords(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True


    def dfs(r, c, node, path):
        if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] not in node.children or (r, c) in visit):
            return
    
        visit.add((r, c))
        path += board[r][c]
        node = node.children[board[r][c]]
        if node.is_end:
            res.add(path)
        dfs(r + 1, c, node, path)
        dfs(r - 1, c, node, path)
        dfs(r, c + 1, node, path)
        dfs(r, c - 1, node, path)
        visit.remove((r, c))

    res = set()
    visit = set()
    for r in range(len(board)):
        for c in range(len(board[0]):
            dfs(r, c, root, "")
    return list(res)
