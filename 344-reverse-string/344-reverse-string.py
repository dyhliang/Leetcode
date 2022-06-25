class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        right = len(s) - 1
        for left in range(len(s)//2):
            s[left], s[right] = s[right], s[left]
            right -= 1
        