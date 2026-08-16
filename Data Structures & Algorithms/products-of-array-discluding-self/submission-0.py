class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProduct = 1
        result = [1] * len(nums)

        for i, n in enumerate(nums):
            result[i] = forwardProduct
            forwardProduct = forwardProduct * n
        
        backwardProduct = 1
        
        for i in range(len(nums) - 1, -1, -1):
            result[i] = backwardProduct * result[i];
            backwardProduct = backwardProduct * nums[i]
        

        return result
        

            
        
        