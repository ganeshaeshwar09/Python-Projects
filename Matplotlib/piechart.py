import calendar
from datetime import datetime

def get_lastday_of_month(year, month):
    last_day = calendar.monthrange(year, month)[1]
    return last_day

year = 2019
month = 12
last_day = get_lastday_of_month(year, month)
print(f"the last day of {month}/{year} is {last_day}")
