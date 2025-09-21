class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Remove digits from stack while conditions are met
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k digits still remain, remove from the end
        stack = stack[:-k] if k else stack
        
        # Convert to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Return "0" if result is empty
        return result if result else "0"
