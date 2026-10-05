class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            parent[root_a] = root_b
            return True
        for a, b in edges:
            if not union(a, b):
                return [a, b]