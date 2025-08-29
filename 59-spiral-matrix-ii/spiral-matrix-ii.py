class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an empty n x n matrix
        matrix = [[0] * n for _ in range(n)]
        
        # Define the boundaries
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1  # Start filling numbers from 1
        
        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Traverse from right to left (if still valid)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # Traverse from bottom to top (if still valid)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix
