class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            res = max(res, r - l + 1)
        return res
        