from collections import deque

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        window = deque([])
        curr_zeroes = 0
        max_window = 0

        for val in nums:
            if val == 1:
                window.append(val)
            elif val == 0 and curr_zeroes < k:
                curr_zeroes += 1
                window.append(val)
            elif val == 0 and curr_zeroes >= k:
                max_window = max(max_window, len(window))

                while window and curr_zeroes >= k:
                    if window[0] == 0:
                        curr_zeroes -= 1
                    window.popleft()

                if k != 0:
                    window.append(val)
                    curr_zeroes += 1

            max_window = max(max_window, len(window))

        return max_window