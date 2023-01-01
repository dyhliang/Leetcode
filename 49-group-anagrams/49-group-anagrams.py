class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        worddict = {}
        
        for word in strs:
            conv_word = ''.join(sorted([*word]))
            if conv_word not in worddict.keys():
                worddict[conv_word] = [word]
            else:
                worddict[conv_word].append(word)
                
        for w in worddict.values():
            res.append(w)
            
        return res
    