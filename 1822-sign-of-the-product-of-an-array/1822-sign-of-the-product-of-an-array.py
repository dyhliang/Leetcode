class Solution:

    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for val in nums:
            product *= val
            
        if product == 0:
            return 0
        else:
            return int(product / abs(product))
