class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobo_digits = ['0', '1', '6', '8', '9']
        replace_digits = {'6': '9',
                         '9': '6'}
        flipped = ""
        
        for digit in num:
            if digit not in strobo_digits:
                return False
        
            if digit in replace_digits:
                flipped += replace_digits[digit]
            else:
                flipped += digit

        return flipped[::-1] == num
    