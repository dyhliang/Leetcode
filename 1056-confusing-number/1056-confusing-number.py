class Solution:
    def confusingNumber(self, n: int) -> bool:
        flip = {"0": "0",
                "1": "1",
               "6": "9",
               "8": "8",
               "9": "6"}
        new_n = ""
        
        for char in str(n)[::-1]:
            if char not in flip.keys():
                return False
            else:
                new_n += flip[char]
                
        return int(new_n) != n
    