class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxheap = []
        for val in gifts:
            heapq.heappush(maxheap, -val)
            
        while k > 0:
            popped = -1 * heapq.heappop(maxheap)
            rem = -int(popped ** 0.5)
            heapq.heappush(maxheap, rem)
            k -= 1
            
        return -sum(maxheap)
    