class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_t = {}
        res = []
        # Store every element after current position into a list that maps to the current element as the key
        for i in range(len(nums2)):
            hash_t[nums2[i]] = nums2[i+1:]

        # Can now use number from nums1 as index in dictionary, check each number's value list, break out when a greater value is found, if k gets to the end, there is no greater number
        for j in range(len(nums1)):
            if len(hash_t[nums1[j]]) == 0:
                res.append(-1)
            else:
                k = 0
                while k < len(hash_t[nums1[j]]):
                    if hash_t[nums1[j]][k] > nums1[j]:
                        break
                    else:
                        k += 1

                if k < len(hash_t[nums1[j]]):
                    res.append(hash_t[nums1[j]][k])
                else:
                    res.append(-1)
                    
        return res
    