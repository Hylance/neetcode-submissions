class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        for r in range(rows):
            dfs(r, 0, pacific)
            dfs(r, cols - 1, atlantic)
        for c in range(cols):
            dfs(0, c, pacific)
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res