class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        fls = [float(v) for v in arr]
        
        for i, n in enumerate(fls):
            if n * 2 in seen or n / 2 in seen:
                return True
            
            seen.add(n)
        
        return False
    