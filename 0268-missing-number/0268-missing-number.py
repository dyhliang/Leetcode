class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)
        occ = [0] * (max_num + 1)
        ans = max_num + 1

        for j in nums:
            occ[j] += 1
            
        for i, n in enumerate(occ):
            if n == 0:
                return i
            
        return ans