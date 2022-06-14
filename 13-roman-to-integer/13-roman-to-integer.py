class Solution:
    def romanToInt(self, s: str):
        vals = {"I": 1, "IV": 4, "V": 5, "IX": 9,
                "X": 10, "XL": 40, "L": 50, "XC": 90,
                "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

        total = 0
        pos = 0

        while pos < len(s):
            curr = vals[s[pos]]
            if (pos < len(s) - 1) and (curr < vals[s[pos + 1]]):
                total += vals[s[pos] + s[pos + 1]]
                pos += 2
            else:
                total += curr
                pos += 1

        return total
