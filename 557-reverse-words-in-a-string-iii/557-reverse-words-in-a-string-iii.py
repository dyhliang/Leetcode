class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        output = ""
        
        for word in s_list:
            output += word[::-1] + " "
            
        # Print all but last index of output to remove the extra space that would otherwise be at the end
        return output[0:len(output)-1]
    