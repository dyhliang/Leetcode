class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        # t is a pointer that constantly update to point to the children of the current character, if any
        t = self.trie
        for char in word:
            if char not in t:
                # if character is not found, add a new key entry
                t[char] = {}
            
            # regardless of whether char is found, t now points to the 
            # children of the current char
            t = t[char]
                
        # The key entry here can be any string value that is not an alphabetical letter preferably, use True to indicate that the insertion is complete.
        t["√"] = True

    def search(self, word: str) -> bool:
        # Same steps as insert to start off
        t = self.trie
        for char in word:
            # Main difference is if the char is not found, return False to break the loop
            if char not in t:
                return False
            
            t = t[char]
            
        # Checks for the completion status for the word if it was fully inserted. 
        return "√" in t


    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for char in prefix:
            if char not in t:
                return False
        
            t = t[char]
        
        # Simply return true if we're able to iterate through without returning False for char not found in t.
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)