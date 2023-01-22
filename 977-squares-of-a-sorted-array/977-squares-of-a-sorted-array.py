class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n - 1

        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                curr = nums[right]
                right -= 1
            else:
                curr = nums[left]
                left += 1

            res[i] = curr ** 2
            
        return res