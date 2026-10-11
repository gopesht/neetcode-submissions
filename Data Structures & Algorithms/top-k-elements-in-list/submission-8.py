class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for n in nums:
            count_map[n] += 1
        
        # buckets = [[] for i in range(len(nums) + 1)]


        # for key, v in count_map.items():
        #     buckets[v].append(key)
        # result = []
        # while k>0:
        #     for n in reversed(buckets):
        #         if n is not None and k>0:
        #             for i in n:
        #                 result.append(i)
        #                 k = k - 1
        #                 if k == 0:
        #                     break

        heap = []

        for n in count_map.keys():
            heapq.heappush(heap, (count_map[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        

        result = []
        for n in range(k):
            result.append(heapq.heappop(heap)[1])

        return result
        