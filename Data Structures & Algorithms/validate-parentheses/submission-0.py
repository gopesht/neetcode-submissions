class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (popped == '{' and c != '}') or (popped == '[' and c != ']') or (popped == '(' and c != ')'):
                    return False
        
        if len(stack) > 0:
            return False
        return True
                
        