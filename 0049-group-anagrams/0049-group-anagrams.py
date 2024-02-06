class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for word in strs:
            sorted_word = ''.join(sorted(list(word)))
            
            if sorted_word not in dic.keys():
                dic[sorted_word] = [word]
            else:
                dic[sorted_word].append(word)
                
        for key in dic:
            res.append(dic[key])
            
        return res