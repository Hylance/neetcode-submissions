class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        def dfs(cur, target, visited):
            if cur == target:
                return 1.0
            visited.add(cur)
            for nei, weight in graph[cur]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return result * weight
            return -1.0
        for (a, b) in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, set()))
        return res