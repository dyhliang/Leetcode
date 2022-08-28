class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip = {"0": "0",
                "1": "1",
               "6": "9",
               "8": "8",
               "9": "6"}
        
        str_n = str(n)
        
        if any(digit in ("2", "3", "4", "5", "7") for digit in str_n):
            return False
        else:
            new_n = ""
            
            for i in range(len(str_n)-1, -1, -1):
                new_n += flip[str_n[i]]

            return int(new_n) != n
