class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0  # correct pos
        cows = 0  # found in secret but not correct pos
        occ = defaultdict(int)

        for pos, char in enumerate(secret):
            if char == guess[pos]:
                bulls += 1
            else:
                cows += int(occ[char] < 0) + int(occ[guess[pos]] > 0)
                occ[char] += 1
                occ[guess[pos]] -= 1

        return f"{bulls}A{cows}B"
    