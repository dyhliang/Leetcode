class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        digits = [*str(n)]
        str_n = ""
        for d in digits:
            if d in flip.keys():
                str_n += flip[d]
            else:
                return False

        new_n = int(str_n[::-1])
        return n != new_n