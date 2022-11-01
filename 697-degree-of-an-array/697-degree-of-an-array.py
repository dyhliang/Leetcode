class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        Understand
            Degree of an array is the max freq of any one of its elements
            Array is guaranteed to be non-empty
            Integers are always positive

        Edge cases:
            Nums arr has: 1 element


        Match
            Hash table
            2 for loops: 1 to set up hash table of indices occurrences, 1 to find the               first indices occurrence array that is the same length value as the                     max_freq

        Plan
            Use hash table to keep track of indices for each unique element in array,               while also keeping tracking of the max freq element

            Shortest length will come from the difference of index -1 and 0 for the                 first indices occurrence array that has the same length as max_freq
        """
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
    