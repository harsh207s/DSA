from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]

            results = []
            for i, char in enumerate(expr):
                if char in "+-*":
                    # Divide expression into left and right parts
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])

                    # Combine the results of left and right using the current operator
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)

            # Base case: if it's just a number (no operators)
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return compute(expression)
