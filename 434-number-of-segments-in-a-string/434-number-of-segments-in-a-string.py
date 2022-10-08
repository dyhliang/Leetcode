class Solution:
    def countSegments(self, s: str) -> int:
        segments = s.split(" ")
        res = [st for st in segments if st != ""]
        return len(res)
        