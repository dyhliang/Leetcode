class Solution:
    def frequencySort(self, s: str) -> str:
        occ = {}
        res = ""

        new_s = set(s)
        # strip all duplicate letters to scan through long strings more efficiently

        for char in new_s:
            if char not in occ.values():
                if s.count(char) in occ.keys():
                    occ[s.count(char)] += char
                else:
                    occ[s.count(char)] = char

        sorted_occ = sorted(occ.keys())

        for val in reversed(sorted_occ):
            for letter in occ[val]:
                res += (val * letter)

        return res
    