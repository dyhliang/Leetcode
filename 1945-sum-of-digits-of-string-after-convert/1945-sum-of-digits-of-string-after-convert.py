class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha_count = ""
        for c in s:
            alpha_count += str(ord(c) - 96)
            
        conv_count = alpha_count
        while k > 0:
            new_count = 0
            for d in conv_count:
                new_count += int(d)
                
            conv_count = str(new_count)
            k -= 1
            
        return int(conv_count)
