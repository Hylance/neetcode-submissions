class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        res = []
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            board[r][c] = "#"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
            board[r][c] = char
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return res