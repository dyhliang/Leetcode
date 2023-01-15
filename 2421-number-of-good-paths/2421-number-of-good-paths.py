class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            UF[find(x)] = find(y)
        
        tree = defaultdict(list)
        # Using a hashmap of set to get the nodes with the same value easily.
        val2Nodes = defaultdict(set)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        
        # Include the one node path in the result, because it is not calculated when we do comb(n,r).
        res = len(vals)
        
        # Sort the value, and start to union the nodes with the current v that we are checking and their neighbors (have smaller values than the current v).
        for v in sorted(val2Nodes.keys()):
            # Union elements with the current v with its neighbor if its neighbor has a value smaller than v.
            # In this way, our unioned element will only have values smaller than or equal to the current v.
            for node in val2Nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node,nei)
            
            # For each group, we need to count the number of elements with value==v in this group.
            groupCount = defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[find(node)] += 1
                
            for root in groupCount.keys():
                # The following two lines are doing the same thing
                # If there are n number of nodes that have value==v in the a group. 
                # The number of paths is the number of combinations for selecting 2 elements from n elements (repetitions are not allowed).
                
                res += comb(groupCount[root],2)
                
                # res += groupCount[root] * (groupCount[root]-1) // 2
        
        return res