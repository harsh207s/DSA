class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces, then split by spaces
        words = s.strip().split()
        return len(words[-1])
