class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # Use built in binary function with XOR
        return bin(x^y).count("1")
    