class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        res = 0
        
        groups = [0] * k
        groups[0] = 1
        
        for num in nums:
            prefix = (prefix + num % k + k) % k
            res += groups[prefix]
            groups[prefix] += 1
            
        return res
    