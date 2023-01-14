class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        table = {}
        
        def find(x):
            table.setdefault(x, x)
            if x != table[x]:
                table[x] = find(table[x])
            
            return table[x]

        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            
            if (rooty > rootx):
                table[rooty] = rootx
            else:
                table[rootx] = rooty
            
        for i in range(len(s1)):
            union(s1[i], s2[i])
            
        res = ""
        for char in baseStr:
            res += find(char)
            
        return res
                
 