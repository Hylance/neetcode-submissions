class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for (u, v, w) in times:
            graph[u].append((v, w))
        res = 0
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        minHeap = [(0, k)]
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if time > dist[node]:
                continue
            for nei, weight in graph[node]:
                newDist = time + weight
                if newDist < dist[nei]:
                    dist[nei] = newDist
                    heapq.heappush(minHeap, (newDist, nei))
        res = max(dist[1:])
        return res if res != float('inf') else -1