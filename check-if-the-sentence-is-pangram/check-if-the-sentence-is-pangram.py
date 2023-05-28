class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters_set = set()
        for char in sentence:
            letters_set.add(char)
            
        return len(letters_set) == 26
    