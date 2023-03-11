class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = defaultdict(int)
        
        for c in s:
            table[c] += 1
        
        res = sum((val // 2) * 2 for val in table.values())

        return min(len(s), res + 1)