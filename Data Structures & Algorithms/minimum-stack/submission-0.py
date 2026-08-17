class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_ele = val
        if self.min_stack:
            min_ele = min(min_ele, self.min_stack[-1])
        self.min_stack.append(min_ele)
        
    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise Exception("Cannot pop from empty stack!!")
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise Exception("Cannot return min from empty stack!!")
        
