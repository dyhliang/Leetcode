class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(x) for x in digits]
        new_num = int(''.join(str_digits)) + 1
        
        new_digits = [int(x) for x in str(new_num)] 
        return new_digits
        