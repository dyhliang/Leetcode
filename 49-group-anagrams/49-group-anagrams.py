class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for word in strs:
            # Strings are immutable, so split the letters into a list, then sort lexicographically
            # to form a new word that serves as the key to hold all other anagrams to the key (if any)
            word_list = [*word]
            word_list.sort()
            lex_word = "".join(word_list)

            if lex_word not in dict.keys():
                dict[lex_word] = [word]
            else:
                dict[lex_word].append(word)

        res = [li for li in dict.values()]
        return res
    