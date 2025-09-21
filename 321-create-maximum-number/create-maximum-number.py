class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # helper: pick max subsequence of length t
        def pick_max(nums, t):
            drop = len(nums) - t
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        # helper: merge two subsequences into largest
        def merge(a, b):
            res = []
            while a or b:
                if a > b:   # lexicographic comparison
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
            return res

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = pick_max(nums1, i)
            part2 = pick_max(nums2, k - i)
            candidate = merge(part1[:], part2[:])  # use copies
            best = max(best, candidate)
        return best
