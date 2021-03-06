class Solution:
    def dayOfYear(self, date: str) -> int:
        date_list = date.split("-")
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])

        # days accumulated by month, originally had 1: 31 and 12: 365 but this 
        # should actually start at 1:0 and 2:31 because 31 days have past once Feb starts
        days_accum = {
            1: 0,
            2: 31,
            3: 59,
            4: 90,
            5: 120,
            6: 151,
            7: 181,
            8: 212,
            9: 243,
            10: 273,
            11: 304,
            12: 334
        }
        
        day_num = days_accum[month] + day

        # Filter at month == 3, don't do day_num > 59 or >= 60 because it adds an extra day already
        if month >= 3:
            if year % 400 == 0:  #1600 and 2000 are leap; 1700, 1800, 1900 are not
                day_num += 1
            elif year % 4 == 0 and year % 100 != 0:
                day_num += 1
        
        return day_num
