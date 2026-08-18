class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        finalResult = []
        i = 0
        while i < len(nums):
            result = self.twoSum(i, nums)
            finalResult.extend(result)
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i = i + 1
            i = i+1
            
        
        return finalResult
        
    

    def twoSum(self, i: int, nums: List[int]) -> List[List[int]]:
        j = i + 1
        first = nums[i]
        k = len(nums) - 1
        result = []

        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                t = [nums[i], nums[j], nums[k]]
                result.append(t)
                while j < k and nums[j] == nums[j+1]:
                    j = j+1
                while j < k and nums[k] == nums[k-1]:
                    k = k - 1
                j = j + 1
                k = k - 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j = j + 1
            elif nums[i] + nums[j] + nums[k] > 0:
                k = k - 1
        
        return result
                
