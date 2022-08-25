from copy import deepcopy


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        occ = {}
        for c in chars:
            occ[c] = 1 + occ.get(c, 0)
        res = 0

        for word in words:
            temp = deepcopy(occ)
            for pos, letter in enumerate(word):
                if letter in occ.keys() and occ[letter] > 0:
                    occ[letter] = occ.get(letter, 0) - 1

                    if pos == len(word) - 1:
                        res += len(word)
                else:
                    break

            occ = temp

        return res
