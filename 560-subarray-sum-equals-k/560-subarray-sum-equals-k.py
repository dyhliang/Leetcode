class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        pref_sum = 0
        table = {0: 1}
        
        for val in nums:
            pref_sum += val
            
            if pref_sum - k in table:
                res += table[pref_sum - k]
            
            if pref_sum not in table:
                table[pref_sum] = 1
            else:
                table[pref_sum] += 1
                
        return res
            