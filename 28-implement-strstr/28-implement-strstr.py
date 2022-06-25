class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle not in haystack:
            return -1
        elif len(haystack) == 0 or len(needle) == 0:
            return 0
        else:
            for m in range(len(haystack)):
                if haystack[m] == needle[0]:
                    if needle == haystack[m:m+len(needle)]:
                        return m
                    