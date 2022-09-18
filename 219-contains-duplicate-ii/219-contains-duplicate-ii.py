class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # There cannot be two distinct indices if there's only 1 value
        # And k = abs(i-j) is at minimum 1
        if len(nums) == 1 or k == 0:
            return False

        val_loc = {}
        for i, val in enumerate(nums):
            if val not in val_loc.keys():
                val_loc[val] = [i]
            else:
                val_loc[val].append(i)


        for key in val_loc.keys():
            if len(val_loc[key]) > 1:
                for pos in range(len(val_loc[key])-1):
                    diff = abs(val_loc[key][pos] - val_loc[key][pos+1])
                    if diff <= k:
                        return True
            
        return False
            