import calendar
from datetime import datetime

def last_day_of_month(year, month):
    last_day = calendar.monthrange(year, month)[0]
    return last_day

year = 2023
month = 3
last_day = last_day_of_month(year, month)
print(f"the last day of the {month}/{year} is {last_day}")