class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_list = [""] * len(s)
        for i, char in enumerate(s):
            new_list[indices[i]] = char

        new_str = "".join(new_list)
        return new_str

    