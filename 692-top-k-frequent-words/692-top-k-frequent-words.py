import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_heap = []
        no_dupes = set(words)
        for word in no_dupes:
            # Creates max_heap with elements inside the list as tuples (-1 * occ, word)
            # heapppush also reduces the need to sort the occs outside of this loop.
            heapq.heappush(max_heap, ((-1 * words.count(word)), word))

        count = 0
        res = []
        while count < k:
            count += 1
            w = heapq.heappop(max_heap)
            res.append(w[1])

        return res
    