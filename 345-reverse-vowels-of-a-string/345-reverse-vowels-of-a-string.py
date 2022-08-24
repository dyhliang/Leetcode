class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_pos = [pos for pos in range(len(s)) if s[pos] in vowels]
        s_chars = [char for char in s]
        
        r = -1
        for l in range(len(vowel_pos) // 2):
            left = vowel_pos[l]
            right = vowel_pos[r]
            s_chars[left], s_chars[right] = s_chars[right], s_chars[left]
            r -= 1
            
        new_s = ''.join(s_chars)
        return new_s
    