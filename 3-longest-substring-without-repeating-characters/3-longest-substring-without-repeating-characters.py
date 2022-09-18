from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Covers cases when s is empty, and when there are no dupes in s
        if len(set(s)) == len(s):
            return len(s)

        # Sliding window approach
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
                # Reduce duplicate substr lengths in the list
                if len(substr) not in sub_list:
                    sub_list.append(len(substr))

                # If the current char is already found in substr, keep popping off the front until we get that same char, then pop one more time
                if char in substr:
                    while substr[0] != char:
                        substr.popleft()

                    substr.popleft()
                
                # Append current character as part of new substr
                substr.append(char)

        # For substrs that don't see a duplicate as it reaches the end of s.
        sub_list.append(len(substr))

        return max(sub_list)
    