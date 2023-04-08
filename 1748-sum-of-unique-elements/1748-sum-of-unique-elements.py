class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for val in nums:
            table[val] += 1
            
        total = 0
        for k in table:
            if table[k] == 1:
                total += k
                
        return total
    