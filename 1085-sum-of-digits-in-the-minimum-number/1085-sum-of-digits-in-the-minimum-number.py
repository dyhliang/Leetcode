class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        minimal = min(nums)
        sum_digits = 0
        for digit in str(minimal):
            sum_digits += int(digit)
            
        return (sum_digits + 1) % 2
    