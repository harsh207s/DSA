from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        res = []

        for i in range(word_len):  # shift starting points
            left = i
            seen = Counter()

            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word in word_count:
                    seen[word] += 1
                    
                    # If word appears more times than allowed, move left pointer
                    while seen[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len

                    # If window matches total length, valid start found
                    if right + word_len - left == total_len:
                        res.append(left)
                else:
                    seen.clear()
                    left = right + word_len

        return res
