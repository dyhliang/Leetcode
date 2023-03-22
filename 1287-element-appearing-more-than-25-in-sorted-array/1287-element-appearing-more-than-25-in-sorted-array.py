class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        table = defaultdict(int)
        
        for val in arr:
            table[val] += 1
            if table[val] > 0.25 * len(arr):
                return val
            