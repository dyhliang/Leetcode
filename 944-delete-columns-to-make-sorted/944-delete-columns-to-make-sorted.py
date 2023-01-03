class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Use list comp to combine letters at each str of same index to make
        # iterating easier
        matrix = [[w[i] for w in strs] for i in range(0, len(strs[0]))]
        count = 0
        for chars in matrix:
            curr_str = "".join(chars)
            sorted_curr_str = "".join(sorted([*curr_str]))

            if curr_str != sorted_curr_str:
                count += 1

        return count