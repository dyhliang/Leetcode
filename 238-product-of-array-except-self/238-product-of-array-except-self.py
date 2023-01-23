import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # If the entire list is 0s, we just return the same list
        res = []
        prod = np.prod(nums)

        # Keep track of alternate product when first 0 in the list is removed
        if 0 in nums:
            new_list = [val for val in nums]
            new_list.remove(0)
            alt_prod = int(np.prod(new_list))

        for val in nums:
            # Didn't say we can't use ^-1 to turn the current value into its reciprocal
            if val != 0:
                recip = val ** -1
                res.append(int(prod * recip))
            else:
                res.append(alt_prod)

        return res
    