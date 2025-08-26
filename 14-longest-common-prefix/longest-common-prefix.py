from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first word as prefix
        prefix = strs[0]
        
        for s in strs[1:]:
            # Shrink prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
