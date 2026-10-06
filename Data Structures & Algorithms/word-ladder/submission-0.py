class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        step = 1
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i + 1:]
                        if new_word in words:
                            words.remove(new_word)
                            q.append(new_word)
            step += 1
        return 0