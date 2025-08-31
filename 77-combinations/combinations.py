class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            # If we formed a valid combination
            if len(path) == k:
                res.append(path[:])  # copy current path
                return
            
            # Try adding numbers from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # undo last choice (backtrack)
        
        backtrack(1, [])
        return res
