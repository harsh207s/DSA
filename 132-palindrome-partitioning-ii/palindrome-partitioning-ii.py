class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Precompute palindrome table
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True  # single char is palindrome
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
        
        # Step 2: DP for minimum cuts
        cuts = [0] * n
        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0  # no cut needed if whole prefix is palindrome
            else:
                cuts[i] = i  # max cuts = i (worst case)
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)
        
        return cuts[-1]
