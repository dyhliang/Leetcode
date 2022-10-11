class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        hmap = {}
        for val in nums:
            if val not in hmap.keys():
                hmap[val] = []
                
            for k in hmap.keys():
                if val > k: 
                    if len(hmap[k]) == 0 or val > hmap[k][-1]:
                        hmap[k].append(val)
                        
                        if len(hmap[k]) == 2:
                            return True
                        
                    elif hmap[k] and val < hmap[k][-1]:
                        hmap[k].pop()
                        hmap[k].append(val)


        return False