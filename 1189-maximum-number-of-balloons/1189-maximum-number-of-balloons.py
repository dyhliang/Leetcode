class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        table = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for c in text:
            if c in table.keys():
                table[c] += 1
                
        if 0 in table.values() or (table['l'] < 2 and table['o'] < 2):
            return 0
        else:
            l_o = min(table['l'] // 2, table['o'] // 2)
            return min(l_o, min(table.values()))
