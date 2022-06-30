class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        modifier = nums[len(nums) // 2]
        moves = 0
        
        for val in nums:
            if val != modifier:
                moves += abs(modifier - val)
        
        return moves
    