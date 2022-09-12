class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        stack = [intervals[0][0], intervals[0][1]]

        for arr in intervals[1:]:
            if arr[0] < stack[-1] <= arr[1]:
                while arr[0] < stack[-1] <= arr[1] and len(stack) > 1:
                    stack.pop()
                    if arr[1] > stack[-1]:
                        stack.append(arr[1])
                        break
            else:
                if arr[0] == stack[-1]:
                    stack.pop()
                    stack.append(arr[1])
                else:
                    if arr[0] > stack[-1]:
                        stack.append(arr[0])

                    if arr[1] >= stack[-1]:
                        stack.append(arr[1])

        res = [[stack[pos], stack[pos+1]] for pos in range(0, len(stack), 2)]
        return res
        