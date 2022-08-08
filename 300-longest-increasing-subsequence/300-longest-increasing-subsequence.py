class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for i in range(1, len(nums)):

            if nums[i] > subseq[-1]:
                subseq.append(nums[i])
            else:
                j = 0
                while subseq[j] < nums[i]:
                    j += 1
                subseq[j] = nums[i]

        return len(subseq)
    