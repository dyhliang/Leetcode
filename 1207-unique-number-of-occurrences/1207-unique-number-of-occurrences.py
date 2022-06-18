class Solution:
    def uniqueOccurrences(self, arr):
        
        # use hash table to store occurrences, adjust index if collision
        occ = {}
        for i in range(len(arr)):
            if arr[i] < 0:
                occ[arr[i] * -7] = 1 + occ.get(arr[i] * -7, 0) 
            else:
                occ[arr[i]] = 1 + occ.get(arr[i], 0) 
        
        # convert occurrences values to a set to weed out duplicates
        occ_keys = occ.keys()
        occ_vals = occ.values()
        return len(occ_keys) == len(set(occ_vals))
    