class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace (handles multiple spaces automatically)
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join with a single space
        return " ".join(words)
