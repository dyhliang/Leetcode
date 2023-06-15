class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.psum = [nums[0]]
        
        for n in nums[1:]:
            total = self.psum[-1] + n
            self.psum.append(total)

    def sumRange(self, left: int, right: int) -> int:
            
        if left > 0:
            return self.psum[right] - self.psum[left - 1]
        else:
            return self.psum[right]
        
        #[-2, -2, 1, -4, -2, -3]
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)