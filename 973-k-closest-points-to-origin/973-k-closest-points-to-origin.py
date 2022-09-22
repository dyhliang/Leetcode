import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for p in points:
            dist = sqrt(p[0] ** 2 + p[1] ** 2)
            heapq.heappush(minheap, [dist, p])
            
        res = []
        while k > 0:
            popped = heapq.heappop(minheap)
            res.append(popped[1])
            k -= 1
        
        return res
        