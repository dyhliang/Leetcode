class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        table = {}
        for val in deck:
            table[val] = 1 + table.get(val, 0)

        # Use the lowest common factor as divisor in modulo later
        cf = min(table.values())

        for card in table:
            if table[card] == 1:
                return False

            # gcf checks if the two numbers can be partitioned into a number that's not 1
            gcf = math.gcd(table[card], cf)
            if gcf == 1:
                return False
            else:
                cf = min(gcf, cf)

        return True