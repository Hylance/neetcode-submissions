class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            if r >= rows or c >= cols or r < 0 or c < 0 or word[index] != board[r][c]:
                return False
            board[r][c] = '#'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                if dfs(r + dr, c + dc, index + 1):
                    return True
            board[r][c] = word[index]
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False