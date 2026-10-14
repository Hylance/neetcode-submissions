class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        dist = [0.0] * n
        dist[start_node] = 1.0
        maxHeap = [(-1.0, start_node)]
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            prob = -prob
            if prob < dist[node]:
                continue
            if node == end_node:
                return prob
            for nei, weight in graph[node]:
                newProb = prob * weight
                if newProb > dist[nei]:
                    dist[nei] = newProb
                    heapq.heappush(maxHeap, (-newProb, nei))
        return 0.0