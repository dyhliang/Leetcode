class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        replace_digits = {'0': '0',
                          '1': '1',
                          '8': '8',
                          '6': '9',
                         '9': '6'}
        replace_num = ""
        
        for digit in num:
            if digit not in replace_digits:
                return False
            
            if digit == '6' or digit == '9':
                replace_num += replace_digits[digit]
            else:
                replace_num += digit

        return replace_num[::-1] == num
    