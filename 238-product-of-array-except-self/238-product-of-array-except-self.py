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
            if val == 0:
            # when there's more than one zero, the product will always be 0
                if nums.count(0) > 1:
                    res.append(0)
                else:
                    res.append(nonzero_prod)    
                    # if there's 1 zero in the list, use nonzero_product
            else:
                res.append(int(product * (val ** -1)))
                # use current number raised to -1 as a workaround

        return res
