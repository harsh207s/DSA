class Solution:
    def calculate(self, s: str) -> int:
        s += "+"  # add a fake operator to process last number
        
        stack = []
        num = 0
        op = "+"  # last seen operator
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch in "+-*/":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    prev = stack.pop()
                    # truncated toward zero
                    stack.append(int(prev / num))
                
                num = 0
                op = ch  # update operator
        
        return sum(stack)
