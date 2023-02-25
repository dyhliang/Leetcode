class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        res = []
        heap = []
        table = defaultdict()
        places = {1: "Gold Medal",
                  2: "Silver Medal",
                  3: "Bronze Medal"}

        for val in score:
            heapq.heappush(heap, -val)

        k = 1
        while heap:
            popped = heapq.heappop(heap)
            table[-popped] = k
            k += 1

        for val in score:
            if table[val] in places.keys():
                res.append(places[table[val]])
            else:
                res.append(str(table[val]))

        return res
    