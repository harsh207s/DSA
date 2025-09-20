class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find potential candidates
        cand1, cand2, count1, count2 = None, None, 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        n = len(nums)
        if nums.count(cand1) > n // 3:
            result.append(cand1)
        if cand2 is not None and nums.count(cand2) > n // 3:
            result.append(cand2)

        return result
