class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        hash_t = {}
        dupes = []
        for val in nums:
            hash_t[val] = hash_t.get(val, 0) + 1

            if hash_t[val] > 1:
                dupes.append(val)

        return dupes
    