class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits_dict = {}
        for n in range(0, 16):
            bits_dict[n] = []

        res = []

        for num in arr:
            bin_num = bin(num)
            ones_count = bin_num.count('1')
            bits_dict[ones_count].append(num)

        for key in bits_dict:
            bits_dict[key].sort()
            res += bits_dict[key]

        return res
