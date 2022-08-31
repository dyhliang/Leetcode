class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        max_heap = [-1 * val for val in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # y is the heavier stone
            y = heapq.heappop(max_heap)
            x = heapq.heappop(max_heap)
            if x != y:
                new_stone = -y - -x
                heapq.heappush(max_heap, -1 * new_stone)

        if len(max_heap) == 0:
            return 0
        else:
            return -1 * heapq.heappop(max_heap)
        