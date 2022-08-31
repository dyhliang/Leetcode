import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        occ = {}
        max_heap = []
        no_dupes = set(nums)

        for n in nums:
            occ[n] = 1 + occ.get(n, 0)

        for val in no_dupes:
            heapq.heappush(max_heap, ((-1 * occ[val]), val))

        res = []
        while k > 0:
            n = heapq.heappop(max_heap)
            res.append(n[1])
            k -= 1

        return res
    