class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num_range = high - low + 1
        
        if low % 2 == 1 and high % 2 == 1:
            return (num_range + 1) // 2
        else:
            return num_range // 2