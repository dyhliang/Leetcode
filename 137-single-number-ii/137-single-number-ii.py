class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        occ = {}
        for val in nums:
            occ[val] = 1 + occ.get(val, 0)
            
        for key in occ:
            if occ[key] == 1:
                return key
        