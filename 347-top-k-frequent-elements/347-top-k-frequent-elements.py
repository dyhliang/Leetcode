import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a dict to keep count of occurrences and maxheap to organize such occurrences
        occ = {}
        maxheap = []
        res = []
        
        for val in nums:
            occ[val] = 1 + occ.get(val, 0)
            
        # Heap is organized by [-1 * occurence, value itself]
        for v in occ.keys():
            hq.heappush(maxheap, [-1 * occ[v], v])
            
        c = 0
        while c < k:
            popped = hq.heappop(maxheap)[1]
            res.append(popped)
            c += 1
            
        return res
    