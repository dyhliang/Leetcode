class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        tree = defaultdict(list)
        for s, e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        def dfs(node, parent) -> int:
        
            res = 0
            for n in tree[node]:
                if n != parent:
                    res += dfs(n, node)

            if res or hasApple[node]:
                return res + 2

            return res

        return max(dfs(0,-1)-2, 0)