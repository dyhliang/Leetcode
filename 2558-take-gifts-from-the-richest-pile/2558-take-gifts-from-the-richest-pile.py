import heapq as hq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = []
        for val in gifts:
            hq.heappush(maxheap, -val)
            
        while k > 0:
            popped = -1 * hq.heappop(maxheap)
            rem = -int(popped ** 0.5)
            hq.heappush(maxheap, rem)
            k -= 1
            
        return -sum(maxheap)
    