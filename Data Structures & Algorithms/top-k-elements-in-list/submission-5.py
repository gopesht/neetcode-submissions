class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
        

        buckets = [None] * (len(nums) + 1)


        for key, v in count_map.items():
            lst = buckets[v]
            if lst is None:
                lst = []
            lst.append(key)
            buckets[v] = lst
        result = []
        while k>0:
            for n in reversed(buckets):
                if n is not None and k>0:
                    for i in n:
                        result.append(i)
                        k = k - 1
                        if k == 0:
                            break

        return result
        