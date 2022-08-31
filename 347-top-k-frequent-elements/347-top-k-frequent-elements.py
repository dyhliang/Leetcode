import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        
        max_heap = []
        no_dupes = set(nums)
        
        for val in no_dupes:
            heapq.heappush(max_heap, ((-1 * nums.count(val)), val))
            
        res = []
        
        while k > 0:
            n = heapq.heappop(max_heap)
            res.append(n[1])
            k -= 1
            
        return res
    