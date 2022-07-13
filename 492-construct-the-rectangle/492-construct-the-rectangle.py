class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        # stores all the factor pairs for area integer into map
        factor_pairs = {val: area // val for val in range(1, int(area ** (1/2)) + 1) if area % val == 0 }

        # The min diff is always found at the last key in the map, since the keys are already sorted, grab the max key
        opt = max(factor_pairs.keys())
        dim_1, dim_2 = opt, factor_pairs[opt]
        
        # L always >= W for all [L, W]
        if dim_2 > dim_1:
            return [dim_2, dim_1]
        else:
            return [dim_1, dim_2]
        