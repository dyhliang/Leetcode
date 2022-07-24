class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_pos = [pos for pos in range(len(s)) if s[pos] in vowels]
        s_chars = [char for char in s]
        
        b = -1
        for i in range(len(vowel_pos) // 2):
            s_chars[vowel_pos[i]], s_chars[vowel_pos[b]] = s_chars[vowel_pos[b]], s_chars[vowel_pos[i]]
            b -= 1
            
        new_s = ''.join(s_chars)
        return new_s
    
    