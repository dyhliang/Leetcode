import heapq as hq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxheap = []
        res = 0

        for val in nums:
            if -val not in maxheap:
                hq.heappush(maxheap, -val)

        if len(maxheap) < 3:
            res = -1 * hq.heappop(maxheap)
        else:
            i = 0
            while i < 3:
                res = -1 * hq.heappop(maxheap)
                i += 1

        return res
    