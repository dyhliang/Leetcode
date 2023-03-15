class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for i, n in enumerate(arr):
            if float(n) * 2 in seen or n / 2 in seen:
                return True
            
            seen.add(float(n))
        
        return False
    