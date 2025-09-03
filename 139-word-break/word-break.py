class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for faster lookup
        n = len(s)

        # dp[i] = True if s[:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always segmentable

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        return dp[n]
