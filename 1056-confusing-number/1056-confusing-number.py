class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip = {"0": "0",
                "1": "1",
               "6": "9",
               "8": "8",
               "9": "6"}
        
        if any(digit in ("2", "3", "4", "5", "7") for digit in str(n)):
            return False
        else:
            new_n = ""
            rev_str = str(n)[::-1]


            for digit in rev_str:
                if digit not in flip.keys():
                    return False
                else:
                    new_n += flip[digit]

            return int(new_n) != n
