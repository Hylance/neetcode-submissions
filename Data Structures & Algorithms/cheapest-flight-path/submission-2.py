class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        minHeap = [(0, src, 0)]
        while minHeap:
            cost, node, flightsUsed = heapq.heappop(minHeap)
            if cost > dist[node][flightsUsed]:
                continue
            if node == dst:
                return cost
            if flightsUsed == k + 1:
                continue
            for nei, price in graph[node]:
                newCost = cost + price
                newFlights = flightsUsed + 1
                if newCost < dist[nei][newFlights]:
                    dist[nei][newFlights] = newCost
                    heapq.heappush(minHeap, (newCost, nei, newFlights))
        return -1