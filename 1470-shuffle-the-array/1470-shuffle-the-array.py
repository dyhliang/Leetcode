class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        x = 0
        y = len(nums) // 2
        
        while x < len(nums) // 2:
            res.append(nums[x])
            res.append(nums[y])
            x += 1
            y += 1
            
        return res
       