class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def dfs(start):
            if start == len(s):
                res.append(path.copy())
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if substring != substring[::-1]:
                    continue
                path.append(substring)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res