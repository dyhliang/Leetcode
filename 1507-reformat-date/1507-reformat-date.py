class Solution:
    def reformatDate(self, date: str) -> str:
        months_map = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
                      "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                      "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        date_list = date.split(" ")     # [day, month, year]
        new_date = ""
        new_date += ((date_list[2] + "-") + (months_map[date_list[1]] + "-"))

        if len(date_list[0]) == 3:      # For days 1-9
            new_date += ("0" + date_list[0][0])
        else:
            new_date += date_list[0][0:2]

        return new_date
    