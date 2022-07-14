class Solution:
    def largestOddNumber(self, num: str) -> str:

        # Pointer starting from ones place
        for i in range(len(num)-1, -1, -1):
            # Don't need to do [0:i+1] because we just need to test current digit is odd/even, helps with time complexity, return on the first digit to be odd
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        
        return ""
            