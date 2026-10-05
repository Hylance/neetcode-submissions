class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            nonlocal count
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return
            parent[root_a] = root_b
            count -= 1
        for a, b in edges:
            union(a, b)
        return count