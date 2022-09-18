from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Covers cases when s is empty, and when there are no dupes in s
        if len(set(s)) == len(s):
            return len(s)

        # Use a seen list to keep track of said values
        # deque for dequeueing from the front
        seen = []
        substr = deque([])
        sub_list = []   # Keeps track of the lengths of each substring

        
        for char in s:
            if char not in seen:
                seen.append(char)
                substr.append(char)
            else:
                # 
                if len(substr) not in sub_list:
                    sub_list.append(len(substr))

                if char in substr:
                    while substr[0] != char:
                        substr.popleft()

                    substr.popleft()
                substr.append(char)

        sub_list.append(len(substr))

        return max(sub_list)