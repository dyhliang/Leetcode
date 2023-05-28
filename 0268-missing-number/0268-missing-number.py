class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        occ = defaultdict(int)
        ans = max_num + 1
        
        for n in range(max_num + 1):
            occ[n] = 0
            
        for j in nums:
            occ[j] += 1
            
        for k in occ:
            if occ[k] == 0:
                return k
            
        return ans