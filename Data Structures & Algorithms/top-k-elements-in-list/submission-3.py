class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nc = {}
        for num in nums:
            nc[num] = 1 + nc.get(num, 0)
        
        arr = []
        for num, cnt in nc.items():
            arr.append([cnt, num])
        
        arr.sort()
        res = []
        while(len(res)) < k:
            res.append(arr.pop()[1])

        return res
