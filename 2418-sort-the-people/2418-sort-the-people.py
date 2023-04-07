import heapq as hq

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxheap = []
        for i, name in enumerate(names):
            hq.heappush(maxheap, [-heights[i], name])
            
        res = []
        while maxheap:
            popped = hq.heappop(maxheap)
            res.append(popped[1])
            
        return res
    