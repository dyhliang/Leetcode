class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        occ_table = dict()
        
        for i in range(len(nums)):
            occ_table[nums[i]] = 1 + occ_table.get(nums[i], 0)
            
            if occ_table[nums[i]] == 2:
                return True
            
        return False