class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        sorted_letters = [c for c in letters]
        sorted_letters.append(target)
        sorted_letters.sort()
        n = len(sorted_letters) - 1
        seen = False
        
        for i in range(n):
            if sorted_letters[i] == target:
                seen = True
            
            if seen and sorted_letters[i] != sorted_letters[i+1]:
                return sorted_letters[i + 1]
            
        return letters[0]
            