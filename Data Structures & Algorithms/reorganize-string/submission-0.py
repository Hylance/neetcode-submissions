class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_val = max(count.values())
        if max_val > (len(s) + 1) // 2:
            return ""
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        res = []
        pre_char = ""
        pre_freq = 0
        while len(heap) > 0:
            freq, char = heapq.heappop(heap)
            res.append(char)
            freq += 1
            if pre_freq < 0:
                heapq.heappush(heap, (pre_freq, pre_char))
            pre_char = char
            pre_freq = freq
        return "".join(res)