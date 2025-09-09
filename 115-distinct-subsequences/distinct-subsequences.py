class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] = number of subsequences of s[i:] that equals t[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case: any s[i:] can match empty t[n:], so dp[i][n] = 1
        for i in range(m + 1):
            dp[i][n] = 1

        # fill table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # choose s[i] or skip it
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # must skip s[i]
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]
