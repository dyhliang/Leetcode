class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        unique_vals = len(set(nums))
        occ_table = {}
        mode_vals = []

        # Fill up occurrences table
        if k in range(1, unique_vals + 1):
            for i in range(len(nums)):
                occ_table[nums[i]] = 1 + occ_table.get(nums[i], 0)
        
        # Make lists of all keys and values, then map to a new list for [key, occurrences], then sort
        keys_list = list(occ_table.keys())
        vals_list = list(occ_table.values())
        mapped_list = [[vals_list[pos], keys_list[pos]] for pos in range(len(keys_list))]
        mapped_list.sort()

        # Iterate backwards from mapped_list by k times
        pos = -1
        while k > 0:
            mode_vals.append(mapped_list[pos][1])
            pos -= 1
            k -= 1

        return mode_vals
