class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_1 = {}
        res = True
        new_s = s.split(" ")

        if len(pattern) != len(new_s):
            return False

        for pos in range(len(pattern)):
            if pattern[pos] not in hash_1.keys() and new_s[pos] not in hash_1.values():
                hash_1[pattern[pos]] = new_s[pos]
            else:
                if pattern[pos] in hash_1.keys():
                    if new_s[pos] != hash_1[pattern[pos]]:
                        res = False

                if new_s[pos] in hash_1.values() and pattern[pos] not in hash_1.keys():
                    res = False

        return res
