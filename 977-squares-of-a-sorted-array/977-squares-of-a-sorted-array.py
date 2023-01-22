class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    # To do it in O(n), find the index of the smallest positive number
    # Then use two pointers, one going to the left and one going to the right
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result