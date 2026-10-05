class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = set()
        count = 0
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count