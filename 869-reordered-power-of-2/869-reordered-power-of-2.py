class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = permutations(str(n))

        for digits in arr:
            binary = bin(int("".join(digits)))
            if digits[0] != '0' and binary.count('1') == 1:
                return True

        return False