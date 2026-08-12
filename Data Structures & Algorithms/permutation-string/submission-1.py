class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        for i in range(len(s2)):
            counts = target.copy()
            for j in range(i, len(s2)):
                if s2[j] not in counts:
                    break
                counts[s2[j]] -= 1
                if counts[s2[j]] == 0:
                    del counts[s2[j]]
                if not counts:
                    return True
        return False
        