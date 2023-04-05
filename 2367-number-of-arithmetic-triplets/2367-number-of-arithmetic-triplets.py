class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        table = {}
        trips = set()
        for i, val in enumerate(nums):
            table[val] = i

        for i, val in enumerate(nums):
            if val - diff in nums and val + diff in nums:
                trips.add((table[val - diff], i, table[val + diff]))

        return len(trips)
    