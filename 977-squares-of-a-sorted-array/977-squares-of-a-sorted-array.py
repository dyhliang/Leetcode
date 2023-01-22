class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
    # To do it in O(n), find the index of the smallest positive number
    # Then use two pointers, one going to the left and one going to the right
        res = []
        start = 0
        min_val = float('inf')

        for i, val in enumerate(nums):
            if 0 <= val < min_val:
                min_val = val
                start = i

        if max(nums) < 0:
            res = [val ** 2 for val in nums[::-1]]
        elif start == 0:
            res = [val ** 2 for val in nums]
        else:
            seen = set()
            left = start - 1
            right = start

            while len(seen) < len(nums):
                if abs(nums[left]) <= abs(nums[right]):
                    if left in seen:
                        res.append(nums[right] ** 2)
                        seen.add(right)
                        if right < len(nums) - 1:
                            right += 1
                    else:
                        res.append(nums[left] ** 2)
                        seen.add(left)

                    if left > 0:
                        left -= 1
                elif abs(nums[right]) < abs(nums[left]):
                    if right in seen:
                        res.append(nums[left] ** 2)
                        seen.add(left)
                        if left > 0:
                            left -= 1
                    else:
                        res.append(nums[right] ** 2)
                        seen.add(right)
                    if right < len(nums) - 1:
                        right += 1

        return res