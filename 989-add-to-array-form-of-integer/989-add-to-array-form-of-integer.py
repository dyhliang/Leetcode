class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        conv_num = "".join([str(dig) for dig in num])
        ans = int(conv_num) + k
        
        conv_ans = [int(d) for d in str(ans)]
        return conv_ans