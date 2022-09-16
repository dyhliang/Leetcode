class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = str(bin(num))[2:]
        new_bin = ""
        swap = {
            "1": "0",
            "0": "1",
        }
        for digit in num_bin:
            new_bin += swap[digit]

        return int(new_bin, 2)