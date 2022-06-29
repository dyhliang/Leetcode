class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        hash_t = {}
        diff_list = []
        
        # set up empty lists in hash table
        for pos in range(len(wordsDict)):
            hash_t[wordsDict[pos]] = []

        # append indices for word1 and word2
        for pos in range(len(wordsDict)):
            if wordsDict[pos] == word1 or wordsDict[pos] == word2:
                hash_t[wordsDict[pos]].append(pos)

        # append all differences of indices between word1 and word2, then find the min
        for v1 in hash_t[word1]:
            for v2 in hash_t[word2]:
                diff_list.append(abs(v2 - v1))

        return min(diff_list)
    