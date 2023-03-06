class Solution:
    def checkString(self, s: str) -> bool:
        table = {'a': [], 'b': []}
        for i, c in enumerate(s):
            table[c].append(i)
        
        if not table['a'] or not table['b']:
            return True
        elif max(table['a']) < min(table['b']):
            return True
        else:
            return False
        