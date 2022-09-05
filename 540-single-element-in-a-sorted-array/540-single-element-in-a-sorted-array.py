class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        occ = {}
        for num in nums:
            occ[num] = 1 + occ.get(num, 0)
            
        for key in occ:
            if occ[key] == 1:
                return key
            
            