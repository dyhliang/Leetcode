class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_lens = [len(word) for word in strs]
        min_len = min(str_lens)
        
        output = ""
        
        for pos in range(min_len):
            for word in strs:
                if pos == min_len or word[pos] != strs[0][pos]:
                    return output

            output += strs[0][pos]
            
        return output
