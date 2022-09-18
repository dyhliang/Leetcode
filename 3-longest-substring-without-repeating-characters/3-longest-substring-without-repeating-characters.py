from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Covers cases when s is empty, and when there are no dupes in s
        if len(set(s)) == len(s):
            return len(s)

        seen = []
        substr = deque([])
        sub_list = []

        for char in s:
            if char not in seen:
                seen.append(char)
                substr.append(char)
            else:
                if len(substr) > 0 and len(substr) not in sub_list:
                    sub_list.append(len(substr))

                if char in substr:
                    while substr[0] != char:
                        substr.popleft()

                    substr.popleft()
                substr.append(char)

        sub_list.append(len(substr))

        return max(sub_list)