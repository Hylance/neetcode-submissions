class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        diag = set()
        cols = set()
        anti_diag = set()
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
            for c in range(n):
                if c in cols or r - c in diag or r + c in anti_diag:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                diag.add(r - c)
                anti_diag.add(r + c)
                dfs(r + 1)
                board[r][c] = "."
                cols.remove(c)
                diag.remove(r - c)
                anti_diag.remove(r + c)
        dfs(0)
        return res