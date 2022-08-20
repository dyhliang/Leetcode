class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sent_lens = [len(sent.split(" ")) for sent in sentences]
        return max(sent_lens)
    