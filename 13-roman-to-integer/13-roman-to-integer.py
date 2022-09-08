class Solution:
    def romanToInt(self, s: str):
        vals = {"I": 1, "IV": 4, "V": 5, "IX": 9,
                "X": 10, "XL": 40, "L": 50, "XC": 90,
                "C": 100, "CD": 400, "D": 500, "CM": 900,
                "M": 1000}

        digits = [char for char in s]
        total = 0
        pos = 0

        while pos < len(digits):
            curr = vals[digits[pos]]

            if (pos < len(digits) - 1) and (curr < vals[digits[pos + 1]]):
                total += vals[digits[pos] + digits[pos + 1]]
                pos += 2
            else:
                total += curr
                pos += 1

        return total