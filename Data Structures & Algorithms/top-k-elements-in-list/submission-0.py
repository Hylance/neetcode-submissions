class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        for item in nums:
            hash_map[item] += 1
        arr = []
        for num, cnt in hash_map.items():
            arr.append([cnt, num])
        arr.sort(reverse=True)
        res = []
        for item in arr:
            if len(res) < k:
                res.append(item[1])
            else:
                break
        return res


        