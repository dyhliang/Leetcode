class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        
        for char in s:
            count[char] += 1
            
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
            
        return -1