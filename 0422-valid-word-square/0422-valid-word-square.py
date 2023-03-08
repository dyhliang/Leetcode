class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        conv_words = []
        max_len = max([len(w) for w in words])

        if max_len != len(words):
            return False

        for w in words:
            if len(w) == max_len:
                conv_words.append(w)
            else:
                w += ((max_len - len(w)) * " ")
                conv_words.append(w)

        alt = []

        for j in range(len(conv_words)):
            curr = ""
            for i in range(len(conv_words)):
                curr += conv_words[i][j]

            alt.append(curr)

        return alt == conv_words
    