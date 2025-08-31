class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(a, b):
            # base case
            if a == b:
                return True
            if sorted(a) != sorted(b):  # pruning
                return False

            n = len(a)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    return True
                # Case 2: Swap
                if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i]):
                    return True
            return False

        return dfs(s1, s2)
