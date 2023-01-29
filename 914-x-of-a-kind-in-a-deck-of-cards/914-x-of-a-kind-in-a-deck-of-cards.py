class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        table = {}
        for val in deck:
            table[val] = 1 + table.get(val, 0)

        lcf = min(table.values())

        for card in table:
            if table[card] == 1:
                return False

            gcf = math.gcd(table[card], lcf)
            if gcf == 1:
                return False
            else:
                lcf = min(gcf, lcf)

        return True