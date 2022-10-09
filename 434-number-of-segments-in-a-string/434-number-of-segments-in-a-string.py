class Solution:
    def countSegments(self, s: str) -> int:
        prev = " "
        count = 0
        for pos, char in enumerate(s):
            if char == " " and prev != " ":
                count += 1

            prev = char

            if char != " " and pos == len(s) - 1:
                count += 1

        return count
