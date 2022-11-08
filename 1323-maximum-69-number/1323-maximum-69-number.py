class Solution:
    def maximum69Number (self, num: int) -> int:
        place = (10 ** (len(str(num)) - 1))

        for digit in str(num):
            if digit == "6":
                return num + (3 * place)
            
            place = place // 10
        
        return num
