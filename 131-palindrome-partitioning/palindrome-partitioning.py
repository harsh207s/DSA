from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            if start == len(s):
                res.append(path[:])  # add a copy of the current path
                return
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])
        return res
