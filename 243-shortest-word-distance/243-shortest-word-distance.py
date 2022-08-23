class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        hash_t = {}

        for i, w in enumerate(wordsDict):
            if w == word1 or w == word2:
                if w not in hash_t.keys():
                    hash_t[w] = [i]
                else:
                    hash_t[w].append(i)

        res = [abs(a - b) for a in hash_t[word1] for b in hash_t[word2]]
        return min(res)
    