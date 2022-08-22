class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:  
        product = 1
        nonzero_prod = 1
        for val in nums:
            product *= val

            if val != 0:
                nonzero_prod *= val

        res = []
        for val in nums:
            if val == 0 and nums.count(0) > 1:
                res.append(0)
            elif val == 0 and nums.count(0) == 1:
                res.append(nonzero_prod)
            else:
                res.append(int(product * (val ** -1)))

        return res
