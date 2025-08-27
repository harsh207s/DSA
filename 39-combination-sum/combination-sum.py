class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # choose candidates[i]
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i+1, because we can reuse same element
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res
