class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash_t = {}
        visited_dest = []
        
        for p in paths:
            if p[0] not in hash_t.keys():
                hash_t[p[0]] = [p[1]]
            else:
                hash_t[p[0]].append(p[1])

            visited_dest.append(p[1])

        for place in visited_dest:
            if place not in hash_t.keys():
                return place
            