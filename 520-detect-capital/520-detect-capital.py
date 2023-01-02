class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lower = False
        
        if not word[0].isupper():
            for char in word[1:]:
                if char.isupper():
                    return False
        else:
            for pos, char in enumerate(word[1:]):
                if not char.isupper():
                    lower = True

                if not char.isupper() and word[1:][pos-1].isupper():
                    return False
            
        return True