class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        #sorted_tasks = sorted(tasks)
        htable = {}
        rounds = 0
        for val in tasks:
            htable[val] = 1 + htable.get(val, 0)

        for diff in htable:
            occ = htable[diff]
            if occ == 1:
                return -1
            elif occ % 3 == 0:
                rounds += (occ // 3)
            else:
            # 13 - three 3s and two 2s: 13 // 3 = 4, 13 % 3 = 1, 
            #      so since its % 3 = 1, take (13 // 3) + (13 % 3) to get the rounds
            # 17 - five 3s and one 2: 17 // 3 = 5, 17 % 3 = 2,
            #      so since its % 3 = 2, take (17 // 3) + (17 % 3) - 1 to get the rounds
            # 25 - seven 3s and two 2s: 25 // 3 = 8, 25 % 3 = 1,
            #      its % 3 = 1 again, take (25 // 3) + (25 % 3) to get the rounds
                if occ % 3 == 2:
                    rounds += ((occ // 3) + (occ % 3) - 1)
                else:
                    rounds += ((occ // 3) + (occ % 3))
        
        return rounds
    