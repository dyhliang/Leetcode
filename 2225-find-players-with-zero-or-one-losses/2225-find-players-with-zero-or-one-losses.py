class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins = defaultdict(int)
        losses = defaultdict(int)
        
        undefeated = []
        oneloss = []
        for m in matches:
            wins[m[0]] += 1
            losses[m[1]] += 1
            
        minplayer = min(min(wins.keys()), min(losses.keys()))
        maxplayer = max(max(wins.keys()), max(losses.keys()))
        
        for n in range(minplayer, maxplayer+1):
            if losses[n] == 0 and wins[n] > 0:
                undefeated.append(n)
            elif losses[n] == 1:
                oneloss.append(n)
                
        return [undefeated, oneloss]