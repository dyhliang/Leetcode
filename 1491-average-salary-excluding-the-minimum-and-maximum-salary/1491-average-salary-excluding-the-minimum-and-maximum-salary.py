class Solution(object):
    def average(self, salary):
        salary.sort()
        return float(sum(salary[1:-1])) / (len(salary)-2)
        