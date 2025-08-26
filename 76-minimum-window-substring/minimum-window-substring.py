from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)  # frequency of chars in t
        have = {}
        required = len(need)  # number of unique chars needed
        formed = 0  # how many unique chars matched so far
        
        l = 0
        res = (float("inf"), 0, 0)  # (window_len, left, right)

        for r, ch in enumerate(s):
            have[ch] = have.get(ch, 0) + 1
            
            if ch in need and have[ch] == need[ch]:
                formed += 1

            # Try to shrink window when all chars matched
            while l <= r and formed == required:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                
                # remove leftmost char
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]
