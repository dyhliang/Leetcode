class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hmap = {}
        max_freq = 0

        for i, val in enumerate(nums):
            if val not in hmap.keys():
                hmap[val] = [i]
            else:
                hmap[val].append(i)

            max_freq = max(max_freq, len(hmap[val]))

        shortest_len = float('inf')
        for arr in hmap.values():
            if len(arr) == max_freq:
                curr_len = arr[-1] - arr[0] + 1
                shortest_len = min(shortest_len, curr_len)

        return shortest_len
    