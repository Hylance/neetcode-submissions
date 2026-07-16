class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            anagram[s[i]] = anagram[s[i]] + 1 if s[i] in anagram else 1
            anagram[t[i]] = anagram[t[i]] - 1 if t[i] in anagram else -1
        for item in anagram.values():
            if item != 0:
                return False
        return True
            