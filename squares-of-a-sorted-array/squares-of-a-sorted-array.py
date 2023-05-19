class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Input: nums = [-4,-1,0,3,10]
        # Output: [0,1,9,16,100]
        l = 0
        r = len(nums) - 1
        ans = []
        
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                ans.append(nums[r] ** 2)
                r -= 1
            else:
                ans.append(nums[l] ** 2)
                l += 1
        
        return ans[::-1]