class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_t = {}
        for val in nums:
            hash_t[val] = 1 + hash_t.get(val, 0) 
            
        for key in hash_t:
            if hash_t[key] >= (len(nums) // 2 + 1):
                return key
            