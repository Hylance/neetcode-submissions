class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(ni, nj))
            return dp[i][j]
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans