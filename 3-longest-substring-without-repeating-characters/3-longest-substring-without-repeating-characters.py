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
        longest = 0  # Keeps track of the longest substring

        for char in s:
            if char not in seen:
                seen.append(char)
                substr.append(char)
            else:

                # If the current char is already found in substr, keep popping off the front until we get that same char, then pop one more time
                if char in substr:
                    while substr[0] != char:
                        substr.popleft()

                    substr.popleft()
                
                # Append current character as part of new substr
                substr.append(char)

            # Update the longest substr count if current substr length is longest
            longest = max(len(substr), longest)

        return longest
    