class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for item in nums:
            hash_map[item] += 1
        heap = []
        for num in hash_map.keys():
            heapq.heappush(heap, (hash_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        