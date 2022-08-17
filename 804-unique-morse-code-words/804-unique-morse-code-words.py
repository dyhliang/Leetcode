class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        
        for s in words:
            morse = ""
            for char in s:
                morse += table[ord(char) - 97]
            
            res.append(morse)
        return len(set(res))
    