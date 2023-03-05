class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occ = defaultdict(int)
        
        for val in nums:
            occ[val] += 1
            if occ[val] == 2:
                return True
            
        return False
    