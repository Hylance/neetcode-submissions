class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        if r < 0:
            return ""
        return values[r][1]
