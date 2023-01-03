class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Use list comp to combine letters at each str of same index to make
        # iterating easier
        matrix = [[w[i] for w in strs] for i in range(0, len(strs[0]))]
        
        count = 0
        for chars in matrix:
            sorted_chars = sorted(chars)

            if chars != sorted_chars:
                count += 1

        return count