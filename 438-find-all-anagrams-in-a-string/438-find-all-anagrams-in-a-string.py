class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_ct = [0] * 26
        s_ct = [0] * 26
        left = 0  # left counter for window
        
        for char in p:
            p_ct[ord(char) - ord('a')] += 1
        
        for i, char in enumerate(s):
            window = s[left:i+1]
            s_ct[ord(char) - ord('a')] += 1

            if len(window) == len(p):
                if p_ct == s_ct:
                    res.append(i - (len(p) - 1))
                    
                s_ct[ord(s[left]) - ord('a')] -= 1
                left += 1

        return res
    