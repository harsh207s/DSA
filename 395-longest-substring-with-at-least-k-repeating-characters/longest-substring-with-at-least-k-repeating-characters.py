class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # Count frequencies
        from collections import Counter
        freq = Counter(s)

        for ch in freq:
            if freq[ch] < k:
                # Split around invalid character
                return max(self.longestSubstring(t, k) for t in s.split(ch))

        # If all characters satisfy the condition
        return len(s)
