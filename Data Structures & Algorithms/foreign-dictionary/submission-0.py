class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in graph}
        q = deque()
        order = []
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for j in range(min(len(word1), len(word2))):
                a = word1[j]
                b = word2[j]
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)
        while q:
            ch = q.popleft()
            order.append(ch)
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(order) != len(indegree):
            return ""
        return "".join(order)