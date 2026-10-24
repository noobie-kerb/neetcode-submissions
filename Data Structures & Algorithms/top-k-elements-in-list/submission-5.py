class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
        
        heap = []
        for num, cnt in d.items():
            heapq.heappush(heap, (d[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        
        return res

