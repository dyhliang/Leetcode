class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        hash_t = {}
        diff_list = []
        for pos in range(len(wordsDict)):
            hash_t[wordsDict[pos]] = []

        for pos in range(len(wordsDict)):
            if wordsDict[pos] == word1 or wordsDict[pos] == word2:
                hash_t[wordsDict[pos]].append(pos)

        for v1 in hash_t[word1]:
            for v2 in hash_t[word2]:
                diff_list.append(abs(v2 - v1))

        return min(diff_list)
    