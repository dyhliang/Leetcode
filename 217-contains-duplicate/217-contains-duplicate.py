class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occ = {}
        for val in nums:
            occ[val] = 1 + occ.get(val, 0)
            if occ[val] == 2:
                return True
            
        return False
    