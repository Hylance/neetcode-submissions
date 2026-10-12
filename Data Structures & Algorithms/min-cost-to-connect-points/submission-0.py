class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        visited = set()
        n = len(points)
        minHeap = [(0, 0)]
        while(len(visited) < n):
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            x1, y1 = points[node]
            for nei in range(n):
                if nei in visited:
                    continue
                x2, y2 = points[nei]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (distance, nei))
        return res