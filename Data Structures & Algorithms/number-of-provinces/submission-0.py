class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        province = 0
        def dfs(city):
            visited.add(city)
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and next_city not in visited:
                    dfs(next_city)
        for i in range(n):
            if i not in visited:
                dfs(i)
                province += 1
        return province
