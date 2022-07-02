class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sums = {"00": "0",
                "11": "0",
                "01": "1",
                "10": "1",
                "100": "1",
                "101": "0",
                "110": "0",
                "111": "1"}

        res = ""
        carry = ""
        if len(a) > len(b):
            b = ((len(a) - len(b)) * "0") + b
        elif len(b) > len(a):
            a = ((len(b) - len(a)) * "0") + a

        pos = len(a) - 1
        while pos >= 0:
            sum_str = carry + a[pos] + b[pos]
            if sum_str == "11" or sum_str == "101" or sum_str == "110" or sum_str == "111":
                carry = "1"
            else:
                carry = ""

            if pos == 0:
                res += (sums[sum_str] + carry)
            else:
                res += sums[sum_str]
            pos -= 1

        return res[::-1]