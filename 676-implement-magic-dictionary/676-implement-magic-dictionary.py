class MagicDictionary:

    def __init__(self):
        self.dict = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict[len(word)].append(word)

    def search(self, searchWord: str) -> bool:
        return any(sum(a!=b for a,b in zip(searchWord, candidate)) == 1 for candidate in self.dict[len(searchWord)])
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)