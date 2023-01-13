class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        adj = [[] for i in range(len(s))]
        self.res = 0

        for i, val in enumerate(parent):
            if val != -1:
                adj[i].append(val)
                adj[val].append(i)


        def dfs(node, parent):
            firstmax, secondmax = -float("inf"), -float("inf")

            for i in adj[node]:
                if i != parent:
                    val = dfs(i, node)
                    if s[node] != s[i]:
                        if val >= firstmax:
                            firstmax, secondmax = val, firstmax
                        elif val > secondmax:
                            secondmax = val

                        self.res = max(self.res, firstmax + secondmax + 1)
                    else:
                        self.res = max(self.res, val)

            return firstmax + 1 if firstmax != -float("inf") else 1


        return max(dfs(0, -1), self.res)