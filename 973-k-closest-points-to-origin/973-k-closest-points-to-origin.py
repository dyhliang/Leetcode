class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        x2, y2 = 0, 0
        res = []
        for p in points:
            dist = ((p[0] - x2) ** 2 + (p[1] - y2) ** 2) ** (1 / 2)
            heapq.heappush(minheap, [dist, p])

        while k > 0:
            popped = heapq.heappop(minheap)[1]
            res.append(popped)
            k -= 1

        return res