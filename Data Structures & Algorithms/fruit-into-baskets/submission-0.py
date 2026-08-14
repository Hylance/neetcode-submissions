class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res = 0, 0
        window = Counter()
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            while len(window) > 2 and l <= r:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
        