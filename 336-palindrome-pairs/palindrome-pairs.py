class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        def is_pal(s):
            return s == s[::-1]

        word_map = {w: i for i, w in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if is_pal(left):
                    rev = right[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([word_map[rev], i])

                if j != len(word) and is_pal(right):
                    rev = left[::-1]
                    if rev in word_map and word_map[rev] != i:
                        res.append([i, word_map[rev]])

        return res