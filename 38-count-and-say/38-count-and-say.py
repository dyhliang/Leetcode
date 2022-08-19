class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for i in range(n-1):
            count = 1
            temp = ""
            for j in range(len(res) - 1):
                if res[j] == res[j+1]:
                    count += 1
                else:
                    temp += str(count) + res[j]
                    count = 1

            temp += str(count) + res[-1]
            res = temp

        return res
    