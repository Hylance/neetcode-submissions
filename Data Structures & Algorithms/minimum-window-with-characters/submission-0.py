class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        count = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(count)
        res, min_len = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in count and window[c] == count[c]:
                have += 1
            while have == need:
                if r - l + 1 < min_len:
                    res = [l, r]
                    min_len = r - l + 1
                window[s[l]] -= 1
                if s[l] in count and  window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if min_len != float('inf') else ""
        