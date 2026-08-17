class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        start = 10**9
        for n in nums:
            hs.add(n)

        result = 0

        for n in nums:
            if n-1 not in hs:
                start = n - 1
                length = 0
                while start + 1 in hs:
                    length = length + 1
                    start = start + 1
                result = max(result, length)
        return result
