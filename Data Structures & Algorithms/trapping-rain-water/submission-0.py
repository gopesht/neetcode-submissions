class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        stack = []
        result = 0
        n = len(height)
        while i < n:
            while stack and height[stack[-1]] <= height[i]:
                mid = height[stack.pop()]
                if stack:
                    left = height[stack[-1]]
                    right = height[i]
                    h = min(left, right) - mid
                    w = i - stack[-1] - 1
                    result += h * w  
            stack.append(i)
            i = i + 1
        
        return result