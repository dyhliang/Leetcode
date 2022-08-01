class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hash_map = {}
        
        for val in nums:
            hash_map[val] = 1 + hash_map.get(val, 0)
            
        res = [num for num in hash_map.keys() if hash_map[num] == 1]
        return res
    