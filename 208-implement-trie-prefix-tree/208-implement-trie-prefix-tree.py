class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
                
        t["_"] = True

    def search(self, word: str) -> bool:
        t = self.trie
        for char in word:
            if char not in t:
                return False
            
            t = t[char]
            
        return "_" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for char in prefix:
            if char not in t:
                return False
        
            t = t[char]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)