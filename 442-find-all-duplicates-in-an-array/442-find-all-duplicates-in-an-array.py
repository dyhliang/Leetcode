class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        table = {}
        res = []
        for val in nums:
            table[val] = 1 + table.get(val, 0)
            
            if table[val] > 1:
                res.append(val)
                
        return res