class Solution:
    def addDigits(self, num: int) -> int:
        sum_digits = 0
        
        while num >= 10:
            for digit in str(num):
                sum_digits += int(digit)
            
            num = sum_digits
            sum_digits = 0
        
        return num
    