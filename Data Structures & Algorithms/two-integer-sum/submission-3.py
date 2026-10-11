class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = defaultdict(int)

        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapping:
                result = []
                result.append(mapping[diff])
                result.append(i)
                return result
            mapping[n] = i
                
        return []
        