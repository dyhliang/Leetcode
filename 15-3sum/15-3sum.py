class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        array.sort()

        # Similar to Two sum, we can use a table
        # look for first number, solve two sum with that first number
        res = set()
        seen = set()
        for i, val in enumerate(array[:-2]):
            l = i + 1
            r = len(array) - 1
            table = {}
            window = array[l:r + 1]
            if val not in seen:
                seen.add(val)
                
                for j, v in enumerate(window):
                    diff = 0 - val - v

                    if v in table.keys():
                        # [key = value, index = j]
                        combo = (val, diff, v)
                        res.add(combo)
                    else:
                        table[diff] = j

        return res
    