class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque([])
        longest = 0

        for char in s:
            if not window or char not in window:
                window.append(char)
            else:
                longest = max(len(window), longest)
                while window and window[0] != char:
                    window.popleft()

                window.popleft()
                window.append(char)

        longest = max(len(window), longest)
        return longest