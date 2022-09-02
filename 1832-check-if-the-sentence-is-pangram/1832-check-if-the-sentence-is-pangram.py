class Solution:
    def checkIfPangram(self, s: str) -> bool:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
        lower_s = s.lower()
        for letter in alpha:
            if letter not in lower_s:
                return False

        return True
    