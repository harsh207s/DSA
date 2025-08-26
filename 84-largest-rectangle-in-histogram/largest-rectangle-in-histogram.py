class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights + [0]):  # add sentinel
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        return max_area
