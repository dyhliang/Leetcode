class Solution:
    def frequencySort(self, s: str) -> str:
        occ = {}
        res = ""

        new_s = set(s)
        # strip all duplicate letters to scan through long strings faster

        # store the occurrences of each letter as the key, the letter as the value 
        for char in new_s:
            if char not in occ.values():
                if s.count(char) in occ.keys():
                    occ[s.count(char)] += char
                else:
                    occ[s.count(char)] = char

        # Can't sort a dictionary, but we can use a separate list to sort its keys (which are ints)
        sorted_occ = sorted(occ.keys())

        # Decreasing order, so iterate backwards from the new occurrences sorted list, and multiply each character for every occ key int by the key int
        for val in reversed(sorted_occ):
            for letter in occ[val]:
                res += (val * letter)

        return res
    
