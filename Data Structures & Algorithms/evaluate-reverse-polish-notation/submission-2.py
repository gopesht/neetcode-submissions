class Solution:
    def is_valid_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if self.is_valid_int(s):
                stack.append(s)
            elif s in ["+", "-", "*", "/"]:
                secondOperand = int(stack.pop()) if stack else None
                firstOperand = int(stack.pop()) if stack else None
                result = 0
                if s == "+":
                    result = firstOperand + secondOperand
                elif s == "*":
                    result = firstOperand * secondOperand
                elif s == "-":
                    result = firstOperand - secondOperand
                else: 
                    result = firstOperand / secondOperand
                stack.append(result)
            
        return int(stack.pop())

            