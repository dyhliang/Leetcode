class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        res = []        
        sorted_nums = sorted(nums)
        curr_arr = [sorted_nums[0]]
        curr_min = min(curr_arr)
        
        for n in sorted_nums[1:]:
            if len(curr_arr) == 3:
                res.append(curr_arr)
                curr_arr = [n]
                curr_min = min(curr_arr)
            elif n - curr_min > k:
                return []
            else:
                curr_min = min(n, curr_min)
                curr_arr.append(n)
                    
        if len(curr_arr) == 3:
            res.append(curr_arr)
        return res
                
        